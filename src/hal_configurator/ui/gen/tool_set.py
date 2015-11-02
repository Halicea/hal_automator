# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/halicea/projects/hal_automator/utils/qtUi/tool_set.ui'
#
# Created: Mon Nov  2 11:05:53 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ToolSet(object):
    def setupUi(self, ToolSet):
        ToolSet.setObjectName("ToolSet")
        ToolSet.resize(162, 541)
        self.verticalLayout = QtGui.QVBoxLayout(ToolSet)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lv_tools = QtGui.QListView(ToolSet)
        self.lv_tools.setViewMode(QtGui.QListView.ListMode)
        self.lv_tools.setModelColumn(0)
        self.lv_tools.setObjectName("lv_tools")
        self.verticalLayout.addWidget(self.lv_tools)
        spacerItem = QtGui.QSpacerItem(20, 538, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(ToolSet)
        QtCore.QMetaObject.connectSlotsByName(ToolSet)

    def retranslateUi(self, ToolSet):
        ToolSet.setWindowTitle(QtGui.QApplication.translate("ToolSet", "Form", None, QtGui.QApplication.UnicodeUTF8))

