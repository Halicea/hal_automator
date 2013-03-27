python C:\pyinstaller\pyinstaller.py --windowed --icon=favicon.ico src\hal_automator.py

xcopy /E dist\hal_automator\* builds\windows\
xcopy /E src\config.conf builds\windows\config.conf
xcopy /E src\empty_bc.json builds\windows\empty_bc.json
xcopy /E plugins builds\windows\plugins\
rmdir dist /q /s
rmdir build /q /s
