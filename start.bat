@echo off
echo ========================================
echo LMN Industries Website
echo ========================================
echo.
echo Starting the application...
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
call venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt --quiet
echo.

REM Initialize database
echo Initializing database...
python -c "from app import app, db; app.app_context().push(); db.create_all(); print('Database initialized!')"
echo.

REM Start the application
echo ========================================
echo Starting Flask server...
echo Open your browser and go to:
echo http://localhost:5000
echo ========================================
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
