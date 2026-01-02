@echo off
REM Quick Start Script for SIP Gateway Configuration (Windows)

echo ==========================================
echo SIP Gateway Configuration - Quick Start
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python 3 is not installed.
    echo Please install Python 3.7 or higher from python.org
    pause
    exit /b 1
)

echo [OK] Python 3 found

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo [OK] Virtual environment created
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/upgrade dependencies
echo Installing dependencies...
python -m pip install -q --upgrade pip
pip install -q -r requirements.txt
echo [OK] Dependencies installed

echo.
echo ==========================================
echo Setup complete! Starting configuration...
echo ==========================================
echo.

REM Run the configuration script
python sip_gateway_config.py

REM Deactivate virtual environment
call venv\Scripts\deactivate.bat

pause
