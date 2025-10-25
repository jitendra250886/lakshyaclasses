@echo off
REM Get current date and time in format YYYY-MM-DD_HH-MM-SS
for /f "tokens=1-4 delims=/ " %%a in ('date /t') do (
    set mydate=%%d-%%b-%%c
)
for /f "tokens=1-2 delims=: " %%a in ('time /t') do (
    set mytime=%%a-%%b
)

REM Replace colon with dash to avoid invalid filename characters
set logname=lakshya_output_%mydate%_%mytime%.log

REM Set output directory to script folder
set output_dir=G:\My Drive\lakshyaclasses\content\3_course_generate_by_prompt

REM Create directory if it doesn't exist
if not exist "%output_dir%" mkdir "%output_dir%"

REM Run Python script and redirect output
python "G:\My Drive\lakshyaclasses\content\3_course_generate_by_prompt\copiolet_promt_to_course_generate.py" > "%output_dir%\%logname%" 2>&1