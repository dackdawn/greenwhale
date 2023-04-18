@echo off
NET SESSION >NUL 2>&1
if %errorlevel% NEQ 0 (
  PowerShell.exe -Command Start-Process '%0' -Verb RunAs
  exit /b
)

python green.py
