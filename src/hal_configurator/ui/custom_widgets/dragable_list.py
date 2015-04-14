'''
Created on Nov 25, 2012

@author: kostamihajlov
'''
from PySide import QtGui, QtCore
import cPickle


class DragableList(QtGui.QListView):

    def ___init__(self, parent=None):
        super(DragableList, self).__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        # self.setDropIndicatorShown(True)
        self.object_format = None

    def set_object_format(self, object_format):
        self.object_format = object_format

    def flags(self, index):
        print('asking for flags')
        flag = QtCore.Qt.ItemIsEnabled
        if index.isValid():
            flag |= QtCore.Qt.ItemIsSelectable \
                | QtCore.Qt.ItemIsUserCheckable \
                | QtCore.Qt.ItemIsEditable \
                | QtCore.Qt.ItemIsDragEnabled \
                | QtCore.Qt.ItemIsDropEnabled
        return flag

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat(self.object_format):
            # event.setDropAction(QtCore.Qt.QMoveAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        event.setDropAction(QtCore.Qt.CopyAction)
        event.accept()

    def startDrag(self, event):
        index = self.indexAt(event.pos())
        if not index.isValid():
            return
        selected = self.model().data(index, QtCore.Qt.UserRole)
        bstream = cPickle.dumps(selected)
        mimeData = QtCore.QMimeData()
        mimeData.setData(self.object_format, bstream)

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        pixmap = self.get_pixmap(index)
        width = 100
        ratio = pixmap.width()/float(width)
        height = pixmap.height()/ratio
        pixmap = pixmap.scaled(width, height)
        drag.setPixmap(pixmap)
        drag.setHotSpot(QtCore.QPoint(0, 0))
        drag.setPixmap(pixmap)
        drag.start(QtCore.Qt.MoveAction)

    def get_pixmap(self, index):
        pixmap = QtGui.QPixmap()
        return pixmap.grabWidget(self, self.rectForIndex(index))

    def mouseMoveEvent(self, event):
        self.startDrag(event)
