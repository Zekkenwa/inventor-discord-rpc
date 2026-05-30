@echo off
cd /d "%~dp0"

:: Check for Administrator privileges
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :admin_granted
) else (
    echo Requesting Administrator privileges to connect to Discord...
    powershell -Command "Start-Process '%~0' -Verb RunAs"
    exit /b
)

:admin_granted
title Autodesk Inventor Discord RPC
echo =========================================
echo    Autodesk Inventor Discord RPC Setup
echo =========================================
echo.
echo Installing/Verifying required Python packages...
python -m pip install -r requirements.txt
echo.
echo Starting Application...
python inventor_rpc.py
pause
