python C:\pyinstaller\pyinstaller.py --windowed --icon=favicon.ico src\hal_automator.py

xcopy /E dist\hal_automator\* builds\windows\
xcopy /E config.conf builds\windows\
xcopy /E plugins builds\windows\plugins\
rmdir dist /q /s
rmdir build /q /s
