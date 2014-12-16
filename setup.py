#! /usr/bin/env python
#
# Copyright (C) 2012 Nuxeo
#

import os
import sys
from datetime import datetime

from distutils.core import setup

def read_version(init_file):
    with open(init_file, 'rb') as f:
        return f.readline().split("=")[1].strip().replace('\'', '')

def update_version(init_file, version):
    with open(init_file, 'wb') as f:
        f.write("__version__ = '%s'\n" % version)

scripts = ["src/hal_automator.py"]
freeze_options = {}

name = 'hal-automator'
packages = [
    'hal_configurator',
    'hal_configurator.lib',
    'hal_configurator.lib.models',
    'hal_configurator.lib.remote_build',
    'hal_configurator.web',
    'hal_configurator.ui',
    'hal_configurator.ui.custom_widgets',
]
package_data = {
    'halicea.data.icons': ['*.png', '*.svg', '*.ico', '*.icns'],
}
script = 'src/hal_automator.py'
icons_home = 'data/icons'
win_icon = os.path.join(icons_home, 'hal_conffigurator_icon_64.ico')
png_icon = os.path.join(icons_home, 'hal_conffigurator_icon_64.png')
osx_icon = os.path.join(icons_home, 'hal_conffigurator_app_icon_128.icns')

if sys.platform == 'win32':
    icon = win_icon
elif sys.platform == 'darwin':
    icon = osx_icon
else:
    icon = png_icon

icons_files = []
static_files = ['src/config.conf', 'src/empty_bc.json']
for filename in os.listdir(icons_home):
    filepath = os.path.join(icons_home, filename)
    if os.path.isfile(filepath):
        icons_files.append(filepath)

old_version = None
init_file = os.path.abspath(os.path.join(
        'src', 'hal_configurator', '__init__.py'))
version = read_version(init_file)

if '--dev' in sys.argv:
    # timestamp the dev artifacts for continuous integration
    # distutils only accepts "b" + digit
    sys.argv.remove('--dev')
    timestamp = datetime.utcnow().isoformat()
    timestamp = timestamp.replace(":", "")
    timestamp = timestamp.replace(".", "")
    timestamp = timestamp.replace("T", "")
    timestamp = timestamp.replace("-", "")
    old_version = version
    # distutils imposes a max 3 levels integer version
    # (+ prerelease markers which are not allowed in a
    # msi package version). On the other hand,
    # msi imposes the a.b.c.0 or a.b.c.d format where
    # a, b, c and d are all 16 bits integers
    version = version.replace('-dev', ".%s" % (
        timestamp[4:8]))
    update_version(init_file, version)
    print "Updated version to " + version

includes = [
    "config",
    "jenkinsapi",
    "requests",
    "pyzqm",
    "PySide",
    "PySide.QtGui",
    "PySide.QtCore",
    "PySide.QtNetwork"
]
excludes = [
    "ipdb",
    "clf",
    "IronPython",
    "pydoc",
    "tkinter",
]

if '--freeze' in sys.argv:
    print "Building standalone executable..."
    sys.argv.remove('--freeze')
    from cx_Freeze import setup, Executable

    # build_exe does not seem to take the package_dir info into account
    sys.path.append('nuxeo-drive-client')

    executables = [Executable(script, base=None)]

    if sys.platform == "win32":
        # Windows GUI program that can be launched without a cmd console
        executables.append(
            Executable(script, targetName="ndrivew.exe", base="Win32GUI",
                       icon=icon, shortcutDir="ProgramMenuFolder",
                       shortcutName="Nuxeo Drive"))
    scripts = []
    # special handling for data files
    package_data = {}
    icons_home = 'data/icons'
    include_files = [(os.path.join(icons_home, f), "icons/%s" % f)
                     for f in os.listdir(icons_home)]
    freeze_options = dict(
        executables=executables,
        options={
            "build_exe": {
                "includes": includes,
                "packages": packages + [
                    "nose",
                ],
                "excludes": excludes,
                "include_files": include_files,
            },
            "bdist_msi": {
                "add_to_path": True,
                "upgrade_code": '{800B7778-1B71-11E2-9D65-A0FD6088709B}',
            },
        },
    )
    # TODO: investigate with esky to get an auto-updateable version but
    # then make sure that we can still have .msi and .dmg packages
    # instead of simple zip files.

elif sys.platform == 'darwin':
    # Under OSX we use py2app instead of cx_Freeze because we need:
    # - argv_emulation=True for nxdrive:// URL scheme handling
    # - easy Info.plit customization
    import py2app  # install the py2app command

    freeze_options = dict(
        app=["src/hal_automator.py"],
        data_files=[('icons', icons_files), ('', static_files)],
        options=dict(
            py2app=dict(
                iconfile=osx_icon,
                argv_emulation=False,
                plist=dict(
                    CFBundleDisplayName="Hal Configurator",
                    CFBundleName="Hal Configurator",
                    CFBundleIdentifier="com.halicea.hal-configurator",
                    LSUIElement=True,  # Do not launch as a Dock application
                    CFBundleURLTypes=[
                        dict(
                            CFBundleURLName='Hal Configurator URL',
                            CFBundleURLSchemes=['halc'],
                        )
                    ]
                ),
                includes=includes,
                excludes=excludes,
            )
        )
    )
setup(
    name=name,
    version=version,
    description="Automator engine from Halicea.",
    author="Halicea",
    author_email="contact@halicea.com",
    url='https://github.com/Halicea/hal_automator',
    packages=packages,
    package_dir={'hal_configurator': 'src/hal_configurator'},
    package_data=package_data,
    scripts=scripts,
    long_description=open('README.rst').read(),
    **freeze_options
)

if old_version is not None:
    update_version(init_file, old_version)
    print "Restored version to " + old_version