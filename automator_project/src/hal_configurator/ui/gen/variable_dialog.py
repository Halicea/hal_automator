# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/variable_dialog.ui'
#
# Created: Sun Dec 22 01:10:29 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(439, 268)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.txtDisplay = QtGui.QLineEdit(Form)
        self.txtDisplay.setObjectName("txtDisplay")
        self.gridLayout.addWidget(self.txtDisplay, 0, 1, 1, 1)
        self.txt_value = QtGui.QLineEdit(Form)
        self.txt_value.setObjectName("txt_value")
        self.gridLayout.addWidget(self.txt_value, 4, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.adminPanel = QtGui.QGroupBox(Form)
        self.adminPanel.setObjectName("adminPanel")
        self.verticalLayout = QtGui.QVBoxLayout(self.adminPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtGui.QLabel(self.adminPanel)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.cmbType = QtGui.QComboBox(self.adminPanel)
        self.cmbType.setObjectName("cmbType")
        self.gridLayout_2.addWidget(self.cmbType, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.adminPanel)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.txt_name = QtGui.QLineEdit(self.adminPanel)
        self.txt_name.setObjectName("txt_name")
        self.gridLayout_2.addWidget(self.txt_name, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbAdminOnly = QtGui.QCheckBox(self.adminPanel)
        self.cbAdminOnly.setObjectName("cbAdminOnly")
        self.horizontalLayout.addWidget(self.cbAdminOnly)
        self.cbRequired = QtGui.QCheckBox(self.adminPanel)
        self.cbRequired.setObjectName("cbRequired")
        self.horizontalLayout.addWidget(self.cbRequired)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.adminPanel)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.adminPanel.setTitle(QtGui.QApplication.translate("Form", "Admin Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAdminOnly.setText(QtGui.QApplication.translate("Form", "Admin Only", None, QtGui.QApplication.UnicodeUTF8))
        self.cbRequired.setText(QtGui.QApplication.translate("Form", "Required", None, QtGui.QApplication.UnicodeUTF8))

