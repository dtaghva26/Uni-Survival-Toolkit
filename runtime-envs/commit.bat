@echo off
cd /d %~dp0\..

:: Build message (removes outer quotes automatically)
set message=%*

:: Remove surrounding quotes if present
set message=%message:"=%

:: Default message
if "%message%"=="" (
    set message=quick commit
)

:: Get current branch
for /f "delims=" %%i in ('git branch --show-current') do set branch=%%i

echo Current branch: %branch%
echo Message: %message%

:: Branch handling
echo %branch% | findstr "feature/" >nul
if %errorlevel%==0 goto commit

if "%branch%"=="develop" goto commit

echo Switching to develop...
git checkout develop
set branch=develop

:commit
git add .

:: ✅ SAFE commit
git commit -m "%message%"

git push origin %branch%

echo Done on %branch%
pause