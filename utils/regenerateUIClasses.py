import sys
import os
from subprocess import call
import pprint
import sys
import time
import logging
import inspect

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

ui_cmd = "pyside-uic -o %s %s"
rcc_cmd = "pyside-rcc -o %s %s"
ui_root = "../src/hal_configurator/ui/gen/"
ui_classes_root ="../src/hal_configurator/ui"
additional_imports = ["../src/hal_configurator/ui/custom_widgets", "../src/hal_configurator/ui"]

ui_class_template ="""
from PySide import QtGui
from gen.%(module_name)s import %(class_name)s

class %(class_name_new)s(QtGui.QWidget, %(class_name)s):
  def __init__(self, *args, **kwargs):
    super(%(class_name_new)s, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(%(class_name_new)s, self).setupUi(self)

  def bindUi(self):
    pass
"""


def main():
  generated = []
  for root, dirs, files in os.walk("."):
    for f in files:
      if f.endswith(".ui"):
        src = os.path.abspath(os.path.join(root, f))
        dst = os.path.abspath(os.path.join(ui_root, f[:-3]+".py"))
        dst_exists = os.path.exists(dst)
        if not dst_exists or os.path.getmtime(src)>=os.path.getmtime(dst):
          print "... Generating", os.path.basename(dst)
          fcmd = ui_cmd%(dst, src)
          call(fcmd, shell=True)
          generated.append(f[:-3])
      elif f.endswith(".qrc"):
        src = os.path.abspath(os.path.join(root, f))
        dst = os.path.abspath(os.path.join(ui_root, f[:-4]+"_rc.py"))
        dst_exists = os.path.exists(dst)
        if not dst_exists or os.path.getmtime(src)>=os.path.getmtime(dst):
          print "... Generating", os.path.basename(dst)
          fcmd = rcc_cmd%(dst, src)
          call(fcmd, shell=True)
  print "importing", os.path.abspath(ui_root)

  sys.path.append(os.path.abspath(ui_root))
  for ai in additional_imports:
    sys.path.append(os.path.abspath(ai))

  for c in generated:
    dst = os.path.abspath(os.path.join(ui_classes_root, c+".py"))
    print dst
    if not os.path.exists(dst):
      class_name = None
      __import__(c)
      members = inspect.getmembers(sys.modules[c], inspect.isclass)
      for name, obj in members:
        if name.startswith("Ui_"):
          class_name = name
      if class_name:
        print name
        f = open(dst, "w")
        s = ui_class_template%{"module_name":c, "class_name":class_name, "class_name_new":class_name[3:]}
        f.write(s)
        f.close()
      else:
        raise Exception("UI class not found")

class PySideGeneratorHandler(FileSystemEventHandler):
  def __init__(self, *args, **kwargs):
    super(PySideGeneratorHandler, self).__init__(*args, **kwargs)

  def on_moved(self, event):
    main()
  def on_created(self, event):
    main()
  def on_deleted(self, event):
    main()
  def on_modified(self, event):
    main()

def server():
    event_handler = PySideGeneratorHandler()
    observer = Observer()
    observer.schedule(event_handler, './qtUi', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
  if "-s" in sys.argv:
    server()
  else:
    main()