@echo off
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" goto run
where py >nul 2>nul
if errorlevel 1 (python -m venv .venv) else (py -3 -m venv .venv)
if errorlevel 1 goto fail
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto fail
:run
echo Open http://127.0.0.1:8501 after the server starts.
".venv\Scripts\python.exe" app\server.py
pause
exit /b
:fail
echo Setup failed. Install Python 3.11 or newer and follow README.md.
pause
