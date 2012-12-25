'''
Created on Nov 25, 2012

@author: kostamihajlov
'''
from PySide import QtGui, QtCore
import pickle
class DropableLineEdit(QtGui.QLineEdit):
    def __init__(self, parent=None):
        super(DropableLineEdit, self).__init__(parent)
        self.setAcceptDrops(True)
        self.object_format = None
    
    def set_object_format(self, object_format):
      self.object_format = object_format

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat(self.object_format):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat(self.object_format):
            event.setDropAction(QtCore.Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        data = event.mimeData()
        bstream = data.data(self.object_format)
        selected = pickle.loads(bstream)
        pos = self.cursorPosition()
        t1 = self.text()[0:pos]
        t2 = self.text()[pos:]
        self.setText(t1+str(selected)+t2)
        event.accept()  