@echo off
REM GIF Creator Tool - Drag and Drop Wrapper
REM Simply drag PNG and BMP files onto this batch file to create an animated GIF

setlocal enabledelayedexpansion

REM Get the directory where this batch file is located
set "SCRIPT_DIR=%~dp0"
set "PYTHON_SCRIPT=%SCRIPT_DIR%giffer.py"

REM Check if Python script exists
if not exist "%PYTHON_SCRIPT%" (
    echo Error: giffer.py not found in %SCRIPT_DIR%
    echo Please make sure giffer.py is in the same folder as this batch file.
    pause
    exit /b 1
)

REM Check if any files were dropped
if "%~1"=="" (
    echo.
    echo ========================================
    echo    GIF Creator Tool - Drag & Drop
    echo ========================================
    echo.
    echo Usage: Drag PNG and BMP files onto this batch file
    echo.
    echo The tool will:
    echo - Process all PNG and BMP files in the order you drag them
    echo - Create an animated GIF in the same folder as the first image
    echo - Use 10 FPS animation speed by default
    echo - Handle transparency and magic pink colors
    echo.
    echo Example: Drag file1.png, file2.bmp, file3.png onto this file
    echo.
    pause
    exit /b 0
)

REM Collect all dropped files
set "FILES="
:collect_files
if "%~1"=="" goto process_files
set "FILES=!FILES! "%~1""
shift
goto collect_files

:process_files
REM Remove leading space
set "FILES=%FILES:~1%"

echo.
echo ========================================
echo    Creating GIF from image files...
echo ========================================
echo.

REM Run the Python script with all the files
python "%PYTHON_SCRIPT%" %FILES%

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo    GIF created successfully!
    echo ========================================
    echo.
    echo Window will close automatically in 3 seconds...
    timeout /t 3 /nobreak >nul
) else (
    echo.
    echo ========================================
    echo    Error creating GIF!
    echo ========================================
    echo.
    echo Press any key to close this window.
    echo.
    pause
)

