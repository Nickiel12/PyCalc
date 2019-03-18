REM ------------------------------------------------------

:Begin
SET dtStamp24=%date:~-4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
@echo off
IF exist "F:\PythonScripts" (
echo F:\PythonScripts exists
) ELSE (
 GOTO:Complete
)
echo %dtStamp24%
mkdir "F:\PythonScripts\%dtStamp24%"
ROBOCOPY "%CD%" "F:\PythonScripts\%dtStamp24%" /MIR /COPY:D /XD "%CD%\kivy_env" "%CD%\phasing out scripts"
GOTO:Complete

:EXIT
@echo folder doesn't exist
PAUSE
EXIT

:USERDENIED
@echo backup canceled
GOTO:Complete

:Complete