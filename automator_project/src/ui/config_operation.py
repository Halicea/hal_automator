from PySide import  QtGui
from gen.config_operation import Ui_OperationWidget
from ui.custom_widgets.dropable_line_edit import DropableLineEdit

class OperationWidget(QtGui.QWidget, Ui_OperationWidget):
  def __init__(self, op, *args, **kwargs):
    super(OperationWidget, self).__init__(*args, **kwargs)
    self.setupUi(self)
    self.op = op
    self.items =[]
    self.bindUi()
    
  def bindUi(self):
    self.la_name.setText(self.op["Code"])
    if self.op.has_key("Type"):
      self.la_description.setText(self.op["Type"])
    else:
      self.la_description.setText("No Type is set!")
      #self.la_description.setStyle("color:red;")
    arguments = self.ltv_content
    for arg in self.op["Arguments"].keys():
      la = arg
      val = self.op["Arguments"][arg]
     
      item = QtGui.QFrame(self)
      layout = QtGui.QHBoxLayout(item)
      layout.setContentsMargins(0, 0, 0, 0)
      self.ltv_content.addWidget(item)
      item.setLayout(layout)
      
      self.items.append(item)
      arg_label = QtGui.QLabel(item)
      arg_label.setMinimumWidth(100)
      arg_box = DropableLineEdit(item)
      if arg =="Resource":
        arg_box.set_object_format("application/x-resource")
      else:
        arg_box.set_object_format("application/x-variable")
      
      layout.addWidget(arg_label)
      layout.addWidget(arg_box)
      
      arg_label.setText(la)
      arg_box.setText(val)
  
      
  def get_dict(self):
    d = {}
    d["Code"]=self.op["Code"]
    if self.op.has_key("Type"):
      d["Type"]=self.op["Type"] 
    args = d["Arguments"] = {}
    for l in self.items:
      key = l.children()[1]
      value = l.children()[2]
      args[key.text()]=value.text()
    return d
    
      
      
    

