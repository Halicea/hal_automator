from PySide import  QtGui
from hal_configurator.ui.gen.config_operation import Ui_OperationWidget
from custom_widgets.dropable_line_edit import DropableLineEdit
from hal_configurator.lib import plugin_loader

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
    c = plugin_loader.get_plugin_cls(self.op)
    self.descriptors = c.get_arg_descriptors()
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
    
    for desc in self.descriptors:
      arg = desc.name
      la = desc.name
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
      if desc.argument_type == "OperationsBundle":
        from config_bundle import BundleWidget
        arg_box = BundleWidget(val, item)
      else:
        if "Resource" in arg:
          arg_box.set_object_format("application/x-resource")
        else:
          arg_box.set_object_format("application/x-variable")
        arg_box.setText(val)
      layout.addWidget(arg_label)
      layout.addWidget(arg_box)
      arg_label.setText(la)  

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
      desc = [x for x in self.descriptors if x.name == key.text()][0]
      if desc.argument_type == 'OperationsBundle':
        value = l.children()[3]
        args[key.text()]=value.get_dict()
      else:
        args[key.text()]=value.text()
    return d

    

