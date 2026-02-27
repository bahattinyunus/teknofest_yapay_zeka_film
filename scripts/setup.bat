@echo off
echo 🎬 Setting up AI Cinematic Universe for Windows...

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.10+ and try again.
    pause
    exit /b
)

:: Create directories
if not exist logs mkdir logs
if not exist outputs mkdir outputs
if not exist assets mkdir assets

:: Virtual Environment
echo 🛠 Creating virtual environment...
python -m venv venv
call .\venv\Scripts\activate

:: Install dependencies
echo 📦 Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

:: Environment configuration
if not exist .env (
    copy .env.example .env
    echo 📁 Created .env file. Please fill in your API keys.
)

echo ✅ Setup complete!
echo 🚀 Use 'venv\Scripts\activate' and then 'python main.py --help'
pause
