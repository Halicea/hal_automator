# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/config_operation.ui'
#
# Created: Mon Dec  2 14:58:38 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_OperationWidget(object):
    def setupUi(self, OperationWidget):
        OperationWidget.setObjectName("OperationWidget")
        OperationWidget.resize(400, 145)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OperationWidget.sizePolicy().hasHeightForWidth())
        OperationWidget.setSizePolicy(sizePolicy)
        OperationWidget.setAcceptDrops(False)
        OperationWidget.setStyleSheet("")
        OperationWidget.setFeatures(QtGui.QDockWidget.DockWidgetClosable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.DockWidgetVerticalTitleBar)
        self.dockWidgetContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setStyleSheet("")
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.la_description = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.la_description.setFont(font)
        self.la_description.setAutoFillBackground(False)
        self.la_description.setStyleSheet("")
        self.la_description.setObjectName("la_description")
        self.verticalLayout_2.addWidget(self.la_description)
        self.verticalLayout.addWidget(self.frame)
        self.ltv_content = QtGui.QVBoxLayout()
        self.ltv_content.setSpacing(0)
        self.ltv_content.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.ltv_content.setContentsMargins(-1, 0, -1, -1)
        self.ltv_content.setObjectName("ltv_content")
        self.verticalLayout.addLayout(self.ltv_content)
        OperationWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(OperationWidget)
        QtCore.QMetaObject.connectSlotsByName(OperationWidget)

    def retranslateUi(self, OperationWidget):
        OperationWidget.setWindowTitle(QtGui.QApplication.translate("OperationWidget", "DockWidget", None, QtGui.QApplication.UnicodeUTF8))

