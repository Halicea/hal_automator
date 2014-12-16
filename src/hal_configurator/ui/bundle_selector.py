
from PySide import QtGui
from hal_configurator.ui.gen.bundle_selector import Ui_bundle_selector

class BundleSelector(QtGui.QGroupBox, Ui_bundle_selector):
  def __init__(self, model, *args, **kwargs):
    super(BundleSelector, self).__init__(*args, **kwargs)
    self.model = model
    self.setupUi()
    self.bindUi()
    

  def toggleAll(self):
    i = 0;
    while self.model.item(i):
      self.model.item(i).setCheckState(self.cbTogleAll.checkState())
      i+=1
      
  
  
  def setupUi(self):
    super(BundleSelector, self).setupUi(self)
    self.cbTogleAll.clicked.connect(self.toggleAll)

  def bindUi(self):
    self.lvBundles.setModel(self.model)
    self.btnSave.clicked.connect(self.save_clicked)
  
  
  def save_clicked(self):
    self.close()
