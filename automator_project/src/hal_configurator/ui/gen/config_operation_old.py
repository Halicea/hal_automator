# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/config_operation_old.ui'
#
# Created: Tue Mar 12 14:31:50 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_OperationWidget(object):
    def setupUi(self, OperationWidget):
        OperationWidget.setObjectName("OperationWidget")
        OperationWidget.resize(692, 228)
        self.verticalLayout_2 = QtGui.QVBoxLayout(OperationWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtGui.QFrame(OperationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background:rgb(124, 175, 255)")
        self.frame.setObjectName("frame")
        self.lth_top = QtGui.QHBoxLayout(self.frame)
        self.lth_top.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.lth_top.setObjectName("lth_top")
        self.rbOperation = QtGui.QRadioButton(self.frame)
        self.rbOperation.setObjectName("rbOperation")
        self.lth_top.addWidget(self.rbOperation)
        self.line = QtGui.QFrame(self.frame)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lth_top.addWidget(self.line)
        self.la_name = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.la_name.sizePolicy().hasHeightForWidth())
        self.la_name.setSizePolicy(sizePolicy)
        self.la_name.setObjectName("la_name")
        self.lth_top.addWidget(self.la_name)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lth_top.addItem(spacerItem)
        self.la_description = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.la_description.sizePolicy().hasHeightForWidth())
        self.la_description.setSizePolicy(sizePolicy)
        self.la_description.setMinimumSize(QtCore.QSize(0, 0))
        self.la_description.setMaximumSize(QtCore.QSize(500, 16777215))
        self.la_description.setObjectName("la_description")
        self.lth_top.addWidget(self.la_description)
        self.btn_delete = QtGui.QToolButton(self.frame)
        self.btn_delete.setObjectName("btn_delete")
        self.lth_top.addWidget(self.btn_delete)
        self.verticalLayout_2.addWidget(self.frame)
        self.ltv_content = QtGui.QVBoxLayout()
        self.ltv_content.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.ltv_content.setObjectName("ltv_content")
        self.verticalLayout_2.addLayout(self.ltv_content)
        self.txtOutput = QtGui.QPlainTextEdit(OperationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOutput.sizePolicy().hasHeightForWidth())
        self.txtOutput.setSizePolicy(sizePolicy)
        self.txtOutput.setMaximumSize(QtCore.QSize(16777215, 10))
        self.txtOutput.setBaseSize(QtCore.QSize(0, 10))
        self.txtOutput.setObjectName("txtOutput")
        self.verticalLayout_2.addWidget(self.txtOutput)

        self.retranslateUi(OperationWidget)
        QtCore.QMetaObject.connectSlotsByName(OperationWidget)

    def retranslateUi(self, OperationWidget):
        OperationWidget.setWindowTitle(QtGui.QApplication.translate("OperationWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.rbOperation.setText(QtGui.QApplication.translate("OperationWidget", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.la_name.setText(QtGui.QApplication.translate("OperationWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("OperationWidget", "-", None, QtGui.QApplication.UnicodeUTF8))

