# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/resourceswindow.ui'
#
# Created: Sun Dec 22 01:10:29 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ResourcesWindow(object):
    def setupUi(self, ResourcesWindow):
        ResourcesWindow.setObjectName("ResourcesWindow")
        ResourcesWindow.resize(183, 570)
        self.verticalLayout = QtGui.QVBoxLayout(ResourcesWindow)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lv_resources = ResourcesList(ResourcesWindow)
        self.lv_resources.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.lv_resources.setObjectName("lv_resources")
        self.verticalLayout.addWidget(self.lv_resources)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add = QtGui.QPushButton(ResourcesWindow)
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
        self.btn_delete = QtGui.QPushButton(ResourcesWindow)
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

        self.retranslateUi(ResourcesWindow)
        QtCore.QMetaObject.connectSlotsByName(ResourcesWindow)

    def retranslateUi(self, ResourcesWindow):
        ResourcesWindow.setWindowTitle(QtGui.QApplication.translate("ResourcesWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))

from resources_list import ResourcesList  # @UnresolvedImport
import images_rc  # @UnusedImport
