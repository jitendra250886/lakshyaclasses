# ==============================================
# LakshyaClasses - Start Dev Environment (PowerShell)
# ==============================================
# Usage: Right-click > Run with PowerShell OR execute: .\start_dev.ps1
# It will:
#  1) Create .venv if missing
#  2) Upgrade pip
#  3) Install/refresh requirements if requirements.txt changed
#  4) Activate venv and leave you in an interactive session
#  5) Set FLASK_APP and FLASK_ENV for this session only

$ErrorActionPreference = 'Stop'
Set-Location -Path $PSScriptRoot

# Check Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
  Write-Error "Python is not in PATH. Install Python 3.10+ and retry."
}

# Create venv if needed
if (-not (Test-Path .venv)) {
  Write-Host "[INFO] Creating virtual environment .venv ..."
  python -m venv .venv
}

# Upgrade pip
try { .\.venv\Scripts\python -m pip install --upgrade pip | Out-Null } catch { Write-Warning "Failed to upgrade pip." }

# Install requirements if changed
if (Test-Path requirements.txt) {
  $hash = (Get-FileHash requirements.txt -Algorithm MD5).Hash
  $hashFile = ".venv/.reqhash"
  $needInstall = $true
  if (Test-Path $hashFile) {
    $old = Get-Content $hashFile -Raw
    if ($old.Trim().ToLower() -eq $hash.ToLower()) { $needInstall = $false }
  }
  if ($needInstall) {
    Write-Host "[INFO] Installing dependencies from requirements.txt ..."
    .\.venv\Scripts\pip install -r requirements.txt
    Set-Content -Path $hashFile -Value $hash
  } else {
    Write-Host "[INFO] Requirements unchanged. Skipping install."
  }
} else {
  Write-Warning "requirements.txt not found. Skipping dependency install."
}

# Activate venv
& .\.venv\Scripts\Activate.ps1
$env:FLASK_APP = 'wsgi.py'
$env:FLASK_ENV = 'development'

Write-Host "`n[READY] Virtual environment activated. Run: flask run" -ForegroundColor Green
