@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"
title Hongrui Homepage Dev Startup

echo.
echo ========================================================
echo    Hongrui Official Website (HRhomepage_vue3) Dev
echo ========================================================
echo.
echo    Website Dev : http://localhost:5175
echo    API Proxy   : /api -^> http://localhost:8080
echo.
echo ========================================================
echo.

REM ============================================================
REM  1.  Ensure dependencies installed
REM ============================================================
echo [1/3] Checking dependencies ...
if not exist "node_modules" (
    echo        Installing dependencies via npm install ...
    call npm install
    if errorlevel 1 (
        echo        [ERROR] npm install failed!
        pause
        exit /b 1
    )
) else (
    echo        [OK] node_modules found
)
echo.

REM ============================================================
REM  2.  Check CMS Backend (FastAPI on port 8080)
REM ============================================================
echo [2/3] Checking CMS Backend ...
powershell -Command "try{$c=New-Object Net.Sockets.TcpClient;$c.Connect('127.0.0.1',8080);$c.Close();exit 0}catch{exit 1}" >nul 2>&1
if %errorlevel% equ 0 (
    echo        [OK] Backend reachable at localhost:8080
) else (
    echo        [WARN] Backend not reachable at localhost:8080
    echo        The site will still start, but will show fallback content.
    echo        Start it with HRCMS_Vue3_demo\start_dev.cmd first for live data.
)
echo.

REM ============================================================
REM  3.  Start Vite Dev Server (port 5175)
REM ============================================================
echo [3/3] Starting Website Dev Server -^> http://localhost:5175
if not exist "package.json" (
    echo        [ERROR] package.json not found!
    pause
    exit /b 1
)
start "HRhomepage-5175" cmd /k "cd /d "%~dp0" && echo Hongrui Homepage starting... && npm run dev"
echo        [OK] Dev server launched in a new window
echo.

REM ============================================================
REM  Open browser
REM ============================================================
echo Waiting for compile ...
timeout /t 6 /nobreak >nul
start http://localhost:5175

echo.
echo ========================================================
echo    Homepage Dev : http://localhost:5175
echo    Close the CMD window to stop the service.
echo ========================================================
echo.

pause
