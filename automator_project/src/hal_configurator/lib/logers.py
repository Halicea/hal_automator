import time
import zmq
import traceback
__author__ = 'Costa Halicea'

class LoggerBase(object):
  def write(self, message, logtype='i'):
    print  message
  def close(self):
    raise NotImplementedError()
  def fileno(self):
    return 1

class ZmqChainedLoger(LoggerBase):
  message_sender = None
  is_binded=False
  def __init__(self, port):
    context = zmq.Context()
    if not ZmqChainedLoger.message_sender:
      ZmqChainedLoger.message_sender = context.socket(zmq.PUB) #@UndefinedVariable

    self.port = port
  #needed for pushing the stdout and stderr into the log
  def fileno(self):
    return 1

  def write(self, text, logtype="i"):
    try:
      if not ZmqChainedLoger.is_binded or ZmqChainedLoger.message_sender.closed:
        self._bind_socket()
        ZmqChainedLoger.is_binded = True
      ZmqChainedLoger.message_sender.send_unicode(text)
    except:
      print text
      print "Exception:", traceback.print_exc()

  def close(self):
    ZmqChainedLoger.message_sender.close()

  def _bind_socket(self):
    ZmqChainedLoger.message_sender.bind("tcp://*:%s"%self.port)
    print "Loger binded, sleeping 2 more seconds..."
    time.sleep(2)
    print "continuing execution"
class SocketIOLogger(LoggerBase):
  def __init__(self, address):
    self.is_connected = False
    self.address = address
    self.pool  = []
  def connect(self):
    pass


class ConsoleLoger(LoggerBase):
  # noinspection PyBroadException
  def write(self, message, logtype="i"):
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

  def write(self, message, logtype="i"):
    self.f.write(message+'\n')

  def close(self):
    self.f.close()
  #needed for pushing the stdout and stderr into the log
  def fileno(self):
    return 1

class CompositeLoger(LoggerBase):
  def __init__(self, *logers):
    self.logers = logers

  def write(self, message, logtype="i"):
    for k in self.logers:
      k.write(message, logtype)

  def close(self):
    for k in self.logers:
      k.close()

  def fileno(self):
    return 1