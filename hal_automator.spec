# -*- mode: python -*-
a = Analysis(['src\\hal_automator.py'],
             pathex=['Z:\\MyProjects\\hal_automator\\automator_project'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\hal_automator', 'hal_automator.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='favicon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'hal_automator'))
app = BUNDLE(coll,
             name=os.path.join('dist', 'hal_automator.app'))
