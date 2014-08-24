# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/variableswindow.ui'
#
# Created: Sun Dec 22 01:10:30 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_VariablesWindow(object):
    def setupUi(self, VariablesWindow):
        VariablesWindow.setObjectName("VariablesWindow")
        VariablesWindow.resize(208, 538)
        self.verticalLayout = QtGui.QVBoxLayout(VariablesWindow)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lv_items = DragableList(VariablesWindow)
        self.lv_items.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.lv_items.setObjectName("lv_items")
        self.verticalLayout.addWidget(self.lv_items)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add = QtGui.QPushButton(VariablesWindow)
        self.btn_add.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_add.setBaseSize(QtCore.QSize(32, 32))
        self.btn_add.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttons/images/Button-Add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon)
        self.btn_add.setIconSize(QtCore.QSize(32, 32))
        self.btn_add.setFlat(True)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_delete = QtGui.QPushButton(VariablesWindow)
        self.btn_delete.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_delete.setBaseSize(QtCore.QSize(32, 32))
        self.btn_delete.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/buttons/images/Button-Delete-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon1)
        self.btn_delete.setIconSize(QtCore.QSize(33, 32))
        self.btn_delete.setFlat(True)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(VariablesWindow)
        QtCore.QMetaObject.connectSlotsByName(VariablesWindow)

    def retranslateUi(self, VariablesWindow):
        VariablesWindow.setWindowTitle(QtGui.QApplication.translate("VariablesWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))

from dragable_list import DragableList  # @UnresolvedImport
import images_rc  # @UnusedImport
