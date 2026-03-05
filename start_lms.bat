@echo off
setlocal
:: Force Python to use UTF-8 for all I/O operations
set PYTHONUTF8=1
:: Force path to the directory where the batch file is located
cd /d "%~dp0"
title LMS AI Assistant - Final Fix for Pip v21

:: 1. Check for Admin Privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [!] Requesting Admin Privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/k cd /d ""%~dp0"" && %~nx0' -Verb RunAs"
    exit /b
)

:: 2. Check FFmpeg Directory (C:\ffmpeg\bin)
set "FFM_BIN=C:\ffmpeg\bin"
if not exist "%FFM_BIN%" (
    echo [ERROR] FFmpeg not found at %FFM_BIN%
    pause
    exit
)

:: 3. Register Environment Variable (System Path)
echo %PATH% | findstr /I /C:"%FFM_BIN%" >nul
if %errorLevel% neq 0 (
    echo [+] Registering FFmpeg...
    setx /M PATH "%PATH%;%FFM_BIN%"
    set "PATH=%PATH%;%FFM_BIN%"
)

:: 4. Virtual Environment (venv) Setup
if not exist "venv" (
    echo [+] Creating virtual environment...
    python -m venv venv || goto ERROR
)
call venv\Scripts\activate || goto ERROR

:: 5. Install Dependencies (Using -q to avoid Progress Bar Encoding Error)
echo [+] Checking and installing requirements...
python -m pip install --upgrade pip -q >nul
pip install -r requirements.txt -q || goto ERROR

:: 6. Run Application
echo ======================================================
echo    Starting LMS AI Assistant...
echo ======================================================
python main.py

pause
exit

:ERROR
echo ======================================================
echo    [CRITICAL ERROR] Execution failed.
echo ======================================================
pause