# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/config_bundle.ui'
#
# Created: Mon Dec  2 14:58:38 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BundleWidget(object):
    def setupUi(self, BundleWidget):
        BundleWidget.setObjectName("BundleWidget")
        BundleWidget.resize(443, 446)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BundleWidget.sizePolicy().hasHeightForWidth())
        BundleWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(BundleWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ltv_children_container = QtGui.QVBoxLayout()
        self.ltv_children_container.setObjectName("ltv_children_container")
        self.scrollArea = QtGui.QScrollArea(BundleWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 439, 442))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top_menu = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        self.top_menu.setObjectName("top_menu")
        self.horizontalLayout = QtGui.QHBoxLayout(self.top_menu)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbBreak = QtGui.QRadioButton(self.top_menu)
        self.rbBreak.setObjectName("rbBreak")
        self.horizontalLayout.addWidget(self.rbBreak)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_add_operation = QtGui.QPushButton(self.top_menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_operation.sizePolicy().hasHeightForWidth())
        self.btn_add_operation.setSizePolicy(sizePolicy)
        self.btn_add_operation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_add_operation.setStyleSheet("")
        self.btn_add_operation.setDefault(True)
        self.btn_add_operation.setFlat(False)
        self.btn_add_operation.setObjectName("btn_add_operation")
        self.horizontalLayout.addWidget(self.btn_add_operation)
        self.verticalLayout_2.addWidget(self.top_menu)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ltv_operations = QtGui.QVBoxLayout()
        self.ltv_operations.setObjectName("ltv_operations")
        self.verticalLayout_3.addLayout(self.ltv_operations)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.ltv_children_container.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.ltv_children_container)

        self.retranslateUi(BundleWidget)
        QtCore.QMetaObject.connectSlotsByName(BundleWidget)

    def retranslateUi(self, BundleWidget):
        BundleWidget.setWindowTitle(QtGui.QApplication.translate("BundleWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.rbBreak.setText(QtGui.QApplication.translate("BundleWidget", "Break", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add_operation.setText(QtGui.QApplication.translate("BundleWidget", "+", None, QtGui.QApplication.UnicodeUTF8))

