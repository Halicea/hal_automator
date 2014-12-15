# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/variable_dialog_old.ui'
#
# Created: Tue Dec  3 19:54:00 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(351, 254)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_name = QtGui.QLineEdit(Dialog)
        self.txt_name.setObjectName("txt_name")
        self.gridLayout.addWidget(self.txt_name, 1, 1, 1, 1)
        self.txt_value = QtGui.QLineEdit(Dialog)
        self.txt_value.setObjectName("txt_value")
        self.gridLayout.addWidget(self.txt_value, 4, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.cmbType = QtGui.QComboBox(Dialog)
        self.cmbType.setObjectName("cmbType")
        self.gridLayout.addWidget(self.cmbType, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.txtDisplay = QtGui.QLineEdit(Dialog)
        self.txtDisplay.setObjectName("txtDisplay")
        self.gridLayout.addWidget(self.txtDisplay, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.cbRequired = QtGui.QCheckBox(Dialog)
        self.cbRequired.setObjectName("cbRequired")
        self.verticalLayout.addWidget(self.cbRequired)
        self.cbAdminOnly = QtGui.QCheckBox(Dialog)
        self.cbAdminOnly.setObjectName("cbAdminOnly")
        self.verticalLayout.addWidget(self.cbAdminOnly)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.cbRequired.setText(QtGui.QApplication.translate("Dialog", "Required", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAdminOnly.setText(QtGui.QApplication.translate("Dialog", "Admin Only", None, QtGui.QApplication.UnicodeUTF8))

