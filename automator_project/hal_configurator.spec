# -*- mode: python -*-
import sys, shutil

root = '/Users/kostamihajlov/MyProjects/hal_automator/automator_project'
build_dir = 'build/ios'

a = Analysis(
      [os.path.join(root,'src','hal_configurator.py'), 
       os.path.join(root,'src','lib/configurator_console.py')],
      pathex=[os.path.join(root, 'src'), '/Users/kostamihajlov/Downloads/pyinstaller',  os.path.join(root, 'src', 'ui', 'custom_widgets')]
      hiddenimports=[],
      hookspath=None
    )

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join(root, build_dir, 'main'),
          debug=False,
          strip=None,
          upx=True,
          console=False )
                                                                                           
version = "0.0.1"

if sys.platform.startswith("darwin"):
  app = BUNDLE(exe,
               name=os.path.join(root, build_dir, 'HalAutomator.app'),
               version=version)
print '*'*50
print os.path.join(root, build_dir, 'HalAutomator.app', 'Contents/Resources/qt_menu.nib')
print '*'*50 

try:
  shutil.copytree(
    '/Library/Frameworks/QtGui.framework/Versions/Current/Resources/qt_menu.nib',
    os.path.join(root, build_dir, 'HalAutomator.app', 'Contents/Resources/qt_menu.nib'))
except Exception, ex:
  print ex

try:
  shutil.copy(
    os.path.join(root, "res/app.icns"),
    os.path.join(root, build_dir, 'HalAutomator.app', 'Contents/Resources/App.icns'))
except Exception, ex:
  print ex
