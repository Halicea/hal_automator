# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/regex_tool.ui'
#
# Created: Sun Dec 22 01:10:29 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_RegexTool(object):
    def setupUi(self, RegexTool):
        RegexTool.setObjectName("RegexTool")
        RegexTool.resize(593, 525)
        self.verticalLayout_3 = QtGui.QVBoxLayout(RegexTool)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txtRegex = QtGui.QLineEdit(RegexTool)
        self.txtRegex.setObjectName("txtRegex")
        self.gridLayout.addWidget(self.txtRegex, 1, 1, 1, 1)
        self.btnRun = QtGui.QPushButton(RegexTool)
        self.btnRun.setObjectName("btnRun")
        self.gridLayout.addWidget(self.btnRun, 1, 2, 1, 1)
        self.txtReplaceWith = QtGui.QLineEdit(RegexTool)
        self.txtReplaceWith.setObjectName("txtReplaceWith")
        self.gridLayout.addWidget(self.txtReplaceWith, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(RegexTool)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(RegexTool)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.cbMultiLine = QtGui.QCheckBox(RegexTool)
        self.cbMultiLine.setChecked(True)
        self.cbMultiLine.setObjectName("cbMultiLine")
        self.gridLayout.addWidget(self.cbMultiLine, 2, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.splitter = QtGui.QSplitter(RegexTool)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.txtTest = QtGui.QPlainTextEdit(self.layoutWidget)
        self.txtTest.setObjectName("txtTest")
        self.verticalLayout_2.addWidget(self.txtTest)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.txtResult = QtGui.QPlainTextEdit(self.layoutWidget1)
        self.txtResult.setObjectName("txtResult")
        self.verticalLayout.addWidget(self.txtResult)
        self.verticalLayout_3.addWidget(self.splitter)

        self.retranslateUi(RegexTool)
        QtCore.QMetaObject.connectSlotsByName(RegexTool)

    def retranslateUi(self, RegexTool):
        RegexTool.setWindowTitle(QtGui.QApplication.translate("RegexTool", "Regex Test Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRun.setText(QtGui.QApplication.translate("RegexTool", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("RegexTool", "Regex:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("RegexTool", "Replace With:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbMultiLine.setText(QtGui.QApplication.translate("RegexTool", "Multiline", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RegexTool", "Test Against:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RegexTool", "Result:", None, QtGui.QApplication.UnicodeUTF8))

