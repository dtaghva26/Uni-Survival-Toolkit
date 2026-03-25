@echo off
setlocal enabledelayedexpansion

cd /d %~dp0\..

:: First argument = feature name
set feature=%1

:: Remaining args = commit message
shift
set message=%*
set message=%message:"=%

:: Defaults
if "%feature%"=="" (
    echo ❌ ERROR: You must provide a feature name
    echo Example: commit login "feat: add auth"
    pause
    exit /b
)

if "%message%"=="" (
    set message=quick commit
)

:: Build branch name
set branch=feature/%feature%

echo Feature: %feature%
echo Branch: %branch%
echo Message: %message%

:: Check current branch
for /f "delims=" %%i in ('git branch --show-current') do set current=%%i

:: If not already on this feature branch → create/switch
if /i not "%current%"=="%branch%" (
    git checkout -b %branch% 2>nul || git checkout %branch%
)

:: Commit flow
git add .
git commit -m "%message%"
git push origin %branch%

echo.
echo ✅ Done on %branch%
pause