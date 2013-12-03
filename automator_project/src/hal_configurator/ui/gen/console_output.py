# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/console_output.ui'
#
# Created: Tue Dec  3 19:53:59 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConsoleOutput(object):
    def setupUi(self, ConsoleOutput):
        ConsoleOutput.setObjectName("ConsoleOutput")
        ConsoleOutput.resize(654, 486)
        self.verticalLayout = QtGui.QVBoxLayout(ConsoleOutput)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_clear = QtGui.QPushButton(ConsoleOutput)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout.addWidget(self.btn_clear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.txt_output = QtGui.QTextEdit(ConsoleOutput)
        self.txt_output.setObjectName("txt_output")
        self.verticalLayout.addWidget(self.txt_output)

        self.retranslateUi(ConsoleOutput)
        QtCore.QMetaObject.connectSlotsByName(ConsoleOutput)

    def retranslateUi(self, ConsoleOutput):
        ConsoleOutput.setWindowTitle(QtGui.QApplication.translate("ConsoleOutput", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_clear.setText(QtGui.QApplication.translate("ConsoleOutput", "Clear", None, QtGui.QApplication.UnicodeUTF8))

