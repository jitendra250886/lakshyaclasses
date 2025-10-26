@echo off
setlocal enableextensions enabledelayedexpansion

REM ==============================================
REM  LakshyaClasses - Start Dev Environment (CMD)
REM ==============================================
REM Usage: Double-click this file or run from CMD.
REM It will:
REM  1) Create .venv if missing. if it doesn’t exist (one‑time).
REM  2) Upgrade pip  (best practice).
REM  3) Install dependencies from requirements.txt only when the file changes (we store an MD5 hash in .venv/.reqhash).
REM  4) Activate the venv and leave you in an interactive shell. Activate the venv and set session-only vars. FLASK_APP=wsgi.py, FLASK_ENV=development
REM  5) Set FLASK_APP and FLASK_ENV for this session only
REM  So, after closing the terminal and coming back later, just run the script again—it activates the venv; it won’t reinstall everything unless requirements.txt changed.

cd /d %~dp0

where python >nul 2>&1 || (
  echo [ERROR] Python is not in PATH. Install Python 3.10+ and retry.
  exit /b 1
)

if not exist .venv (
  echo [INFO] Creating virtual environment .venv ...
  python -m venv .venv || (echo [ERROR] venv creation failed & exit /b 1)
)

call .venv\Scripts\python -m pip install --upgrade pip >nul || (
  echo [WARN] Failed to upgrade pip. Continuing...
)

if exist requirements.txt (
  for /f "skip=1 tokens=*" %%H in ('certutil -hashfile requirements.txt MD5 ^| find /i /v "md5"') do set REQHASH=%%H
  if not exist .venv\.reqhash (
    set NEEDINSTALL=1
  ) else (
    set /p OLDHASH=<.venv\.reqhash
    if /i not "!OLDHASH!"=="!REQHASH!" set NEEDINSTALL=1
  )
  if defined NEEDINSTALL (
    echo [INFO] Installing dependencies from requirements.txt ...
    call .venv\Scripts\pip install -r requirements.txt || (
      echo [ERROR] pip install failed. Check requirements.txt.
      exit /b 1
    )
    > .venv\.reqhash echo !REQHASH!
  ) else (
    echo [INFO] Requirements unchanged. Skipping install.
  )
) else (
  echo [WARN] requirements.txt not found. Skipping dependency install.
)

call .venv\Scripts\activate
set FLASK_APP=wsgi.py
set FLASK_ENV=development

echo.
echo [READY] Virtual environment activated.
echo        Run: flask run

echo Opening an interactive shell with the environment active...
cmd /k
