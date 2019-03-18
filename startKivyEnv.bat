@echo off

call "%CD%\kivy_env\Scripts\activate.bat"

@echo on

DOSKEY r=KivyGui.py ^&^& "%CD%\batch_files\KivyBackup.bat"
DOSKEY deact = "%CD%\env\kivy_Scripts\deactivate.bat" ^&^& PAUSE ^&^& exit
@echo %CD%\kivy_env\Scripts

cmd \k

