import time
import zmq
__author__ = 'kostamihajlov'


class ZmqChainedLoger(object):
  def __init__(self, port):
    context = zmq.Context()
    self.message_sender = context.socket(zmq.PUB)
    self.is_binded=False
    self.port = port

  def write(self, text, type="i"):
    try:
      if not self.is_binded:
        self._bind_socket()
        self.is_binded = True
      self.message_sender.send_unicode(text)
    except Exception, ex:
      print "Exception:", str(ex)

  def _bind_socket(self):
    self.message_sender.bind("tcp://*:%s"%self.port)
    print "Loger binded, sleeping 2 more seconds..."
    time.sleep(2)
    print "continuing execution"

class ConsoleLoger(object):
  def write(self, message, t="i"):
    print message
