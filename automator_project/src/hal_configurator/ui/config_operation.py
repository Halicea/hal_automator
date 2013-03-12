from PySide import  QtGui
from gen.config_operation import Ui_OperationWidget
from custom_widgets.dropable_line_edit import DropableLineEdit

class OperationWidget(QtGui.QDockWidget, Ui_OperationWidget):
  def __init__(self, bundle_widget,op, *args, **kwargs):
    """
    :param bundle_widget:
    :type bundle_widget: BundleWidget
    :param op:
    :type op: dict
    :param args:
    :param kwargs:
    """
    super(OperationWidget, self).__init__(*args, **kwargs)
    self.op = op
    self.bundle_widget = bundle_widget
    self.items =[]
    self.setupUi()
    self.bindUi()


  def setupUi(self):
    super(OperationWidget,self).setupUi(self)

  def bindUi(self):
    self.setWindowTitle(self.op["Code"])
    #self.la_name.setText(self.op["Code"])
    if self.op.has_key("Description"):
      self.la_description.setText(self.op["Description"])
    else:
      self.la_description.setText("No Description is set!")
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
      if "Resource" in arg:
        arg_box.set_object_format("application/x-resource")
      else:
        arg_box.set_object_format("application/x-variable")
      layout.addWidget(arg_label)
      layout.addWidget(arg_box)
      arg_label.setText(la)
      arg_box.setText(val)

  def closeEvent(self, *args, **kwargs):
    self.bundle_widget.remove_operation(self)
      
  def get_dict(self):
    d = {}
    d["Code"]=self.op["Code"]
    d["Description"]=self.la_description.text()
    args = d["Arguments"] = {}
    for l in self.items:
      key = l.children()[1]
      value = l.children()[2]
      args[key.text()]=value.text()
    return d
    
      
      
    

