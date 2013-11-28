import time
import zmq
import traceback
__author__ = 'Costa Halicea'

class LoggerBase(object):
  def write(self, message):
    print  message
  def close(self):
    raise NotImplementedError()
  def fileno(self):
    return 1

class ZmqChainedLoger(LoggerBase):
  def __init__(self, port):
    context = zmq.Context()
    self.message_sender = context.socket(zmq.PUB) #@UndefinedVariable
    self.is_binded=False
    self.port = port
  #needed for pushing the stdout and stderr into the log
  def fileno(self):
    return 1

  def write(self, text, logtype="i"):
    try:
      if not self.is_binded:
        self._bind_socket()
        self.is_binded = True
      self.message_sender.send_unicode(text)
    except:
      print text
      print "Exception:", traceback.print_exc()

  def close(self):
    self.message_sender.close()

  def _bind_socket(self):
    self.message_sender.bind("tcp://*:%s"%self.port)
    print "Loger binded, sleeping 2 more seconds..."
    time.sleep(2)
    print "continuing execution"

class ConsoleLoger(LoggerBase):
  # noinspection PyBroadException
  def write(self, message, t="i"):
    try:
      print message
    except:
      pass

  #needed for pushing the stdout and stderr into the log
  def fileno(self):
    return 1

  def close(self):
    pass

class FileLoger(LoggerBase):
  def __init__(self, f):
    self.f = open(f, "a")

  def write(self, message, t="i"):
    self.f.write(message+'\n')

  def close(self):
    self.f.close()
  #needed for pushing the stdout and stderr into the log
  def fileno(self):
    return 1

class CompositeLoger(LoggerBase):
  def __init__(self, *logers):
    self.logers = logers

  def write(self, message, t="i"):
    for k in self.logers:
      k.write(message, t)

  def close(self):
    for k in self.logers:
      k.close()

  def fileno(self):
    return 1