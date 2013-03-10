# -*- mode: python -*-
a = Analysis(['t2s_configurator.py'],
             pathex=['Z:\\MyProjects\\hal_automator\\automator_project\\src'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\t2s_configurator', 't2s_configurator.exe'),
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
               name=os.path.join('dist', 't2s_configurator'))
app = BUNDLE(coll,
             name=os.path.join('dist', 't2s_configurator.app'))
