
from PySide import QtGui, QtCore
from hal_configurator.ui.gen.config_operation_old import Ui_OperationWidget
from custom_widgets.dropable_line_edit import DropableLineEdit
from hal_configurator.lib import plugin_loader

class OperationWidget(QtGui.QWidget, Ui_OperationWidget):
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
    self.plugin_class = plugin_loader.get_plugin_cls(self.op['Code'])
    self.descriptors = self.plugin_class.get_arg_descriptors()
    self.bundle_widget = bundle_widget
    self.items =[]
    self.setupUi()
    self.bindUi()


  def setupUi(self):
    super(OperationWidget,self).setupUi(self)
    self.btn_toggle.clicked.connect(self.toggle)

  def bindUi(self):
    #self.la_name.setText(self.op["Code"])
    self.la_name.setText(self.plugin_class.get_name())
    if self.op.has_key("Description"):
      self.la_description.setText(self.op["Description"])
    else:
      self.la_description.setText("No Description is set!")

    for desc in self.descriptors:
      arg = desc.name
      la = desc.name
      val=None
      if arg in self.op["Arguments"]:
        val = self.op["Arguments"][arg]
      item = QtGui.QFrame(self)
      layout = QtGui.QHBoxLayout(item)
      layout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
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
        arg_box.set_vertical_scroll(False)
      else:
        if "Resource" in arg:
          arg_box.set_object_format("application/x-resource")
        else:
          arg_box.set_object_format("application/x-variable")
          arg_box.setFixedHeight(30)
        arg_box.setText(val)
      layout.addWidget(arg_label)
      layout.addWidget(arg_box)
      arg_label.setText(la)
    self.is_toggled = False
    self.toggle()

  def closeEvent(self, *args, **kwargs):
    self.bundle_widget.remove_operation(self)

  def toggle(self):
    tgl = self.is_toggled
    self.is_toggled = not self.is_toggled
    if tgl:
      self.groupBox.show()
    else:
      self.groupBox.hide()
    self.updateGeometry()


  def sizeHint(self):
    s = None
    if self.is_toggled:
      s = QtCore.QSize(super(OperationWidget,self).sizeHint().width(), 50)
    else:
      s = QtCore.QSize(super(OperationWidget,self).sizeHint().width(), 50+ 50+self.groupBox.sizeHint().height())
    return s

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
