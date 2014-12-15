# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/bundle_execution_progress.ui'
#
# Created: Sun Dec 22 01:10:27 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 97)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.laBundleName = QtGui.QLabel(Form)
        self.laBundleName.setObjectName("laBundleName")
        self.verticalLayout.addWidget(self.laBundleName)
        self.pbProgress = QtGui.QProgressBar(Form)
        self.pbProgress.setProperty("value", 24)
        self.pbProgress.setObjectName("pbProgress")
        self.verticalLayout.addWidget(self.pbProgress)
        self.laInfo = QtGui.QLabel(Form)
        self.laInfo.setObjectName("laInfo")
        self.verticalLayout.addWidget(self.laInfo)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.laBundleName.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.laInfo.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

