from PySide import QtCore

__author__ = 'kostamihajlov'


class ConfigRunnerThread(QtCore.QThread):
  def __init__(self, builder):
    super(ConfigRunnerThread, self).__init__()
    self.builder = builder

  def run(self):
    print "running..."
    try:
      self.builder.apply()
    except:
      raise
    finally:
      self.builder.logger.close()