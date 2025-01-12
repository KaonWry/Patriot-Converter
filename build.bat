@echo off
REM Step 1: Ensure a virtual environment is set up
if not exist venv (
    python -m venv env
    echo Virtual environment created.
)

REM Step 2: Activate the virtual environment
call venv\Scripts\activate

REM Step 3: Upgrade pip
echo Upgrading pip...
pip install --upgrade pip

REM Step 4: Install required dependencies (including PyInstaller)
echo Installing dependencies...
pip install -r requirements.txt
pip install pyinstaller

REM Step 5: Build the app with PyInstaller
echo Building the app...
pyinstaller --onedir --name "Patriot Converter" --noconsole main.py ^
--add-data "ui/conversion_window.ui;ui" ^
--add-data "ui/main_window.ui;ui"

REM Step 6: Notify user of completion
echo Build complete! The executable can be found in the 'dist' folder.
pause