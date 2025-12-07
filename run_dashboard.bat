@echo off
echo 🇳🇵 Digital Divide Nepal Dashboard Launcher
echo ============================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python and try again
    pause
    exit /b 1
)

REM Check if virtual environment is activated
if not defined VIRTUAL_ENV (
    echo 💡 Activating virtual environment...
    if exist "venv\Scripts\activate.bat" (
        call venv\Scripts\activate.bat
        echo ✅ Virtual environment activated
    ) else (
        echo ⚠️  Virtual environment not found, using system Python
    )
)

REM Check if Streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo ❌ Streamlit is not installed
    echo Installing required packages...
    pip install -r requirements.txt
)

echo 🚀 Starting dashboard...
echo 🌐 Dashboard will open at: http://localhost:8501
echo.
echo 📋 Dashboard Features:
echo    - District comparison analysis
echo    - Predictive modeling
echo    - Prescriptive recommendations
echo    - Interactive visualizations
echo.
echo 🛑 Press Ctrl+C to stop the dashboard
echo ============================================
echo.

REM Start the dashboard
python -m streamlit run digital_divide_dashboard.py --server.port 8501

pause