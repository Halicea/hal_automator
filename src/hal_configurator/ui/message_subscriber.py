from PySide import QtCore
from hal_configurator.ui.zmq_listener import ZeroMQ_Listener

__author__ = 'kostamihajlov'


class MessageSubsriberThread (QtCore.QThread):
  on_message_received = QtCore.Signal(str)
  def __init__(self, port):
    super(MessageSubsriberThread, self).__init__()
    self.port = port
  def run(self):
    self.zeromq_listener = ZeroMQ_Listener("tcp://127.0.0.1:%s"%self.port)
    self.zeromq_listener.on_message_recieved.connect(self.message_received)
    print "Subscriber Thread is listening for messages"
    self.zeromq_listener.loop()

  def message_received(self, message):
    self.on_message_received.emit(message)