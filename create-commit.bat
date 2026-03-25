@echo off
setlocal enabledelayedexpansion

:: Get full message
set msg=%*
set msg=%msg:"=%

if "%msg%"=="" (
    echo Provide a message
    exit /b
)

:: Build feature name from message
set feature=%msg%
set feature=!feature: =-!
set feature=!feature::=-!
set feature=!feature:,=-!
set feature=!feature:.=-!
set feature=!feature:/=-!

:: Call main script
runtime-envs\commit.bat !feature! "%msg%"