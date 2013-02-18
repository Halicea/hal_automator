__author__ = 'kostamihajlov'
from PySide import QtCore
import zmq

class ZeroMQ_Listener(QtCore.QObject):
  on_message_recieved = QtCore.Signal(str)

  def __init__(self, address):
    super(ZeroMQ_Listener, self).__init__()
    # Socket to talk to server
    context = zmq.Context()
    print "Listening for messages"
    self.socket = context.socket(zmq.SUB)
    self.socket.setsockopt(zmq.SUBSCRIBE, '')
    self.socket.connect(address)
    self.running = True

  def loop(self):
    while self.running:
      msg = self.socket.recv()
      print msg
      self.on_message_recieved.emit(unicode(msg))
