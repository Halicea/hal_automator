# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/halicea/projects/hal_automator/utils/qtUi/config_operation_old.ui'
#
# Created: Mon Nov  2 11:05:48 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_OperationWidget(object):
    def setupUi(self, OperationWidget):
        OperationWidget.setObjectName("OperationWidget")
        OperationWidget.resize(555, 186)
        OperationWidget.setMinimumSize(QtCore.QSize(300, 30))
        OperationWidget.setStyleSheet("QGroupBox#groupBox{\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0.011, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(101, 101, 101, 255));\n"
"}\n"
"\n"
"QFrame#frame{\n"
"background:rgb(70, 70, 70);\n"
"border-top-left-radius: 9px;\n"
"border-top-right-radius: 9px;\n"
"}\n"
"\n"
"{\n"
"text-color:white;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QtGui.QVBoxLayout(OperationWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(OperationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 30))
        self.frame.setBaseSize(QtCore.QSize(200, 15))
        self.frame.setStyleSheet("background:rgb(70, 70, 70);\n"
"border-top-left-radius: 9px;\n"
"border-top-right-radius: 9px;")
        self.frame.setObjectName("frame")
        self.lth_top = QtGui.QHBoxLayout(self.frame)
        self.lth_top.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.lth_top.setContentsMargins(5, 5, 5, 5)
        self.lth_top.setObjectName("lth_top")
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
        self.rbOperation = QtGui.QRadioButton(self.frame)
        self.rbOperation.setObjectName("rbOperation")
        self.lth_top.addWidget(self.rbOperation)
        self.line = QtGui.QFrame(self.frame)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lth_top.addWidget(self.line)
        self.btn_toggle = QtGui.QToolButton(self.frame)
        self.btn_toggle.setStyleSheet("font: 15pt \".SF NS Text\";")
        self.btn_toggle.setObjectName("btn_toggle")
        self.lth_top.addWidget(self.btn_toggle)
        self.btn_delete = QtGui.QToolButton(self.frame)
        self.btn_delete.setObjectName("btn_delete")
        self.lth_top.addWidget(self.btn_delete)
        self.verticalLayout.addWidget(self.frame)
        self.groupBox = QtGui.QGroupBox(OperationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ltv_content = QtGui.QVBoxLayout()
        self.ltv_content.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.ltv_content.setContentsMargins(0, 0, 0, 0)
        self.ltv_content.setObjectName("ltv_content")
        self.verticalLayout_2.addLayout(self.ltv_content)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(OperationWidget)
        QtCore.QMetaObject.connectSlotsByName(OperationWidget)

    def retranslateUi(self, OperationWidget):
        OperationWidget.setWindowTitle(QtGui.QApplication.translate("OperationWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.la_name.setText(QtGui.QApplication.translate("OperationWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.rbOperation.setText(QtGui.QApplication.translate("OperationWidget", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_toggle.setText(QtGui.QApplication.translate("OperationWidget", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_toggle.setShortcut(QtGui.QApplication.translate("OperationWidget", "X, X", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("OperationWidget", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setShortcut(QtGui.QApplication.translate("OperationWidget", "X", None, QtGui.QApplication.UnicodeUTF8))

