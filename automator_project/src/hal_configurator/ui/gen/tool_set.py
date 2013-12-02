# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/tool_set.ui'
#
# Created: Mon Dec  2 14:58:40 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
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
        self.lv_tools.setObjectName("lv_tools")
        self.verticalLayout.addWidget(self.lv_tools)
        spacerItem = QtGui.QSpacerItem(20, 538, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(ToolSet)
        QtCore.QMetaObject.connectSlotsByName(ToolSet)

    def retranslateUi(self, ToolSet):
        ToolSet.setWindowTitle(QtGui.QApplication.translate("ToolSet", "Form", None, QtGui.QApplication.UnicodeUTF8))

