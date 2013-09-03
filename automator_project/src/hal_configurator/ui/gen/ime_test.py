# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/ime_test.ui'
#
# Created: Mon Jan 28 00:32:42 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ImeForm(object):
    def setupUi(self, ImeForm):
        ImeForm.setObjectName("ImeForm")
        ImeForm.resize(400, 300)
        self.pushButton = QtGui.QPushButton(ImeForm)
        self.pushButton.setGeometry(QtCore.QRect(130, 130, 114, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(ImeForm)
        QtCore.QMetaObject.connectSlotsByName(ImeForm)

    def retranslateUi(self, ImeForm):
        ImeForm.setWindowTitle(QtGui.QApplication.translate("ImeForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ImeForm", "OK", None, QtGui.QApplication.UnicodeUTF8))

