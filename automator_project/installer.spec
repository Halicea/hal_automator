# -*- mode: python -*-
import sys, shutil
 
root = 'src'
 
a = Analysis(
 [
  'hal_configurator.py'
 ],
 pathex=[root])
 
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join(root, 'dist', 'main'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
 
version = "0.0.1"
 

app = BUNDLE(exe,
             name=os.path.join(root, 'dist', 'HalAutomator.app'),
             version=version)
print '*'*50
print  os.path.join(root, 'dist', 'appname.app', 'Contents/Resources/qt_menu.nib')
print '*'*50

shutil.copytree(
    '/Library/Frameworks/QtGui.framework/Versions/Current/Resources/qt_menu.nib',
    os.path.join(root, 'dist', 'appname.app', 'Contents/Resources/qt_menu.nib'))

shutil.copy(
    os.path.join(root, "res/app.icns"),
    os.path.join(root, 'dist', 'appname.app', 'Contents/Resources/App.icns'))
