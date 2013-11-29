# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/resource_dialog.ui'
#
# Created: Thu Nov 28 22:51:09 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ResourceDialog(object):
    def setupUi(self, ResourceDialog):
        ResourceDialog.setObjectName("ResourceDialog")
        ResourceDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(ResourceDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(ResourceDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.txtName = QtGui.QLineEdit(ResourceDialog)
        self.txtName.setObjectName("txtName")
        self.horizontalLayout_2.addWidget(self.txtName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gvView = QtGui.QGraphicsView(ResourceDialog)
        self.gvView.setAutoFillBackground(True)
        brush = QtGui.QBrush(QtGui.QColor(0, 122, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.gvView.setBackgroundBrush(brush)
        self.gvView.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.gvView.setObjectName("gvView")
        self.verticalLayout.addWidget(self.gvView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSave = QtGui.QPushButton(ResourceDialog)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnCancel = QtGui.QPushButton(ResourceDialog)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnChange = QtGui.QPushButton(ResourceDialog)
        self.btnChange.setObjectName("btnChange")
        self.horizontalLayout.addWidget(self.btnChange)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ResourceDialog)
        QtCore.QMetaObject.connectSlotsByName(ResourceDialog)

    def retranslateUi(self, ResourceDialog):
        ResourceDialog.setWindowTitle(QtGui.QApplication.translate("ResourceDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ResourceDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("ResourceDialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("ResourceDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnChange.setText(QtGui.QApplication.translate("ResourceDialog", "Change", None, QtGui.QApplication.UnicodeUTF8))

