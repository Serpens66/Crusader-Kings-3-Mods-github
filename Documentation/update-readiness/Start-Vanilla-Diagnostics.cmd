@echo off
setlocal
echo CK3 Vanilla-Diagnose: Steam muss laufen. CK3 und den Paradox-Launcher vorher schliessen.
echo Ein normaler Debugstart. Im Hauptmenue Konsole oeffnen: dump_data_types
echo Nach dem Export CK3 normal beenden. Vorhandene Script-Exporte bleiben erhalten.
echo Dieses Fenster bis zum Abschluss offen lassen. Keine Maus-/Tastatursteuerung.
"D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe" -B "%~dp0tools\diagnostic_start.py"
set "diagnostic_exit=%ERRORLEVEL%"
echo.
if not "%diagnostic_exit%"=="0" echo Diagnose unvollstaendig. Details stehen oben und im jeweiligen run.json.
echo Abschluss. Dieses Fenster kann jetzt geschlossen werden.
pause
exit /b %diagnostic_exit%
