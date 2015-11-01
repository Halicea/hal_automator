
from PySide import QtGui, QtCore
from hal_configurator.ui.config_operation_old import OperationWidget
import pickle

class ContentFrame(QtGui.QFrame):
    def __init__(self, *args, **kwargs):
        self.ops = []
        self.object_format = 'application/x-plugin'
        super(ContentFrame, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)
    
    def set_bundle(self, bundle):
        self.bundle = bundle
        for op in self.bundle["Operations"]:
            self.add_operation(op)
    
    def add_operation(self, op):
        if not isinstance(op, dict):
           op = op.get_empty_dict() 
        # k = op.get_empty_dict()
        op = OperationWidget(self, op, self)
        #op.btn_delete.clicked.connect(self.delete_clicked)
        self.ops.append(op)
        self.layout().addWidget(op)        
    
    def get_dict(self):
        res = {}
        res["Name"] = self.bundle["Name"]
        ops = res["Operations"] = []
        for op in self.ops:
            ops.append(op.get_dict())
        return res
    def remove_operation(self, op):
        l = [x for x in self.ops if x == op ]
        if len(l)>0:
            self.ops.remove(op)
            op.deleteLater()
        
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
        op = pickle.loads(bstream)
        self.add_operation(op)
        event.accept()
    
    
   
   