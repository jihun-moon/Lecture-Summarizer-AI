@echo off
:: 0. UTF-8 설정 및 경로 강제 고정 (핵심!)
chcp 65001 >nul
setlocal
cd /d "%~dp0"
title LMS AI Assistant - Final Fix

:: 1. 관리자 권한 체크 및 승격
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [!] 환경 변수 등록을 위해 관리자 권한으로 다시 실행합니다...
    powershell -Command "Start-Process cmd -ArgumentList '/k %~f0' -Verb RunAs"
    exit /b
)

:: 2. 다시 한번 경로 고정 (관리자 권한으로 뜬 새 창에서도 적용되게)
cd /d "%~dp0"

:: 3. FFmpeg 경로 확인 (C:\ffmpeg\bin)
set "FFM_BIN=C:\ffmpeg\bin"
if not exist "%FFM_BIN%" (
    echo.
    echo ❌ 에러: %FFM_BIN% 폴더를 찾을 수 없습니다!
    pause
    goto ERROR
)

:: 4. 환경 변수 등록
echo %PATH% | findstr /I /C:"%FFM_BIN%" >nul
if %errorLevel% neq 0 (
    echo [+] FFmpeg 경로를 시스템 Path에 등록합니다...
    setx /M PATH "%PATH%;%FFM_BIN%"
    set "PATH=%PATH%;%FFM_BIN%"
)

:: 5. 가상환경 및 라이브러리 체크
if not exist "venv" (
    echo [+] 가상환경 생성 중...
    python -m venv venv || goto ERROR
)
call venv\Scripts\activate || goto ERROR

echo [+] 라이브러리 상태 체크 및 업데이트 중...
python -m pip install --upgrade pip
pip install -r requirements.txt || goto ERROR

:: 6. 실행
echo.
echo ======================================================
echo    🚀 모든 세팅 완료! 프로그램을 시작합니다.
echo ======================================================
python main.py

pause
exit

:ERROR
echo.
echo ⚠️ 에러 발생! 위 메시지를 확인하세요.
pause