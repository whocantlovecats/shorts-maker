@echo off
REM Quick install script for Windows

echo 🎬 Installing Shorts Maker...

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Install from https://python.org
    pause
    exit /b 1
)

REM Check FFmpeg
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo ⚠️  FFmpeg not found. See SETUP.md for installation
    pause
    exit /b 1
)

REM Install Python packages
echo 📦 Installing dependencies...
pip install -r requirements.txt

echo.
echo ✅ Installation complete!
echo.
echo 📝 Next steps:
echo 1. Get API key: https://aistudio.google.com/app/apikeys
echo 2. Edit config.txt and paste your key
echo 3. Run: python run_shorts_maker.py
echo.
pause
