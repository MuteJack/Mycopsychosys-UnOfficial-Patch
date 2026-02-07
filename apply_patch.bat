@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

:: ============================================
:: Mycopsychosys Remastered - Patch Applier
:: Uses bundled PortableGit (no git installation required)
:: ============================================

set "SCRIPT_DIR=%~dp0"
set "GAME_ROOT=%SCRIPT_DIR%..\\"

set "GIT_DIR=%SCRIPT_DIR%PortableGit"
set "GIT_EXE=%GIT_DIR%\cmd\git.exe"
set "DAT_FILE=%SCRIPT_DIR%unofficial_patch_20260207.dat"
set "TEMP_PATCH=%TEMP%\~unofficial_patch.tmp"

echo ============================================
echo  Mycopsychosys Remastered - Patch Applier
echo ============================================
echo.
echo  Path: !SCRIPT_DIR!
echo.

:: Extract PortableGit if not already extracted
if exist "!GIT_EXE!" goto :skip_extract

set "FOUND_EXE="
for %%F in ("!GIT_DIR!\PortableGit-*.7z.exe") do set "FOUND_EXE=%%F"
if not defined FOUND_EXE (
    echo [ERROR] PortableGit folder does not contain git or a PortableGit installer.
    echo         Download the portable version of Git from the website, and paste to 'Patcher/PortableGit' folder.
    echo         You can download "Git for Windows/x64 Portable." from https://git-scm.com/install/windows
    pause
    exit /b 1
)
echo [0] Extracting PortableGit...
echo PortableGit File: !FOUND_EXE!
"!FOUND_EXE!" -o"!GIT_DIR!" -y
if not exist "!GIT_EXE!" (
    echo [ERROR] Failed to extract PortableGit.
    pause
    exit /b 1
)
echo [OK] Extracting PortableGit has been completed.
echo.

:skip_extract

:: Check encoded patch file
if not exist "!DAT_FILE!" (
    echo [ERROR] !DAT_FILE! not found.
    pause
    exit /b 1
)

:: Check game folder in parent directory
if not exist "!GAME_ROOT!game" (
    echo [ERROR] 'game' folder not found in parent directory.
    echo         Please place the Patcher folder inside the game's root directory.
    echo         Example:
    echo         C:\Program Files ^(x86^)\Steam\steamapps\common\Mycopsychosys Remastered
    echo         D:\SteamLibrary\steamapps\common\Mycopsychosys Remastered
    pause
    exit /b 1
)

:: Step 1: Decode Base64 patch
echo [1/2] Decoding patch data...
powershell -Command "$b64 = [System.IO.File]::ReadAllText('!DAT_FILE!'); $bytes = [Convert]::FromBase64String($b64); [System.IO.File]::WriteAllBytes('!TEMP_PATCH!', $bytes)"

if not exist "!TEMP_PATCH!" (
    echo [ERROR] Failed to decode patch data.
    pause
    exit /b 1
)

:: Step 2: Apply patch from game root
echo [2/2] Applying patch...
cd /d "!GAME_ROOT!"
"!GIT_EXE!" apply -p1 "!TEMP_PATCH!"
set "APPLY_EXIT=!errorlevel!"

:: Cleanup temp file
del "!TEMP_PATCH!" 2>nul

if "!APPLY_EXIT!" neq "0" (
    echo.
    echo [ERROR] Failed to apply patch.
    echo         The game files may be a different version, or the patch has already been applied.
    pause
    exit /b 1
)

echo.
echo [OK] Patch applied successfully!
echo.
pause
