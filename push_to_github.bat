@echo off
setlocal

:: 获取当前时间作为 commit message
for /f "tokens=1-5 delims=/:. " %%a in ("%date% %time%") do (
    set YYYY=%%a
    set MM=%%b
    set DD=%%c
    set HH=%%d
    set MIN=%%e
)
set MSG=auto: update on %YYYY%-%MM%-%DD% %HH%:%MIN%

:: 执行 Git 命令
git add .
git commit -m "%MSG%"
git push origin main

pause
