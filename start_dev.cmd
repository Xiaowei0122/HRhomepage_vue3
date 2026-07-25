@echo off
echo ========================================
echo   HRhomepage Vue3 - Start Dev Server
echo ========================================
echo.

if not exist "node_modules\" (
    echo [1/2] Installing dependencies...
    call npm install
    if errorlevel 1 (
        echo Dependency installation failed. Please check npm config.
        pause
        exit /b 1
    )
    echo Dependencies installed!
) else (
    echo [1/2] Dependencies already exist, skipping install.
)
echo.

echo [2/2] Starting Vite dev server...
echo.
call npm run dev

pause
