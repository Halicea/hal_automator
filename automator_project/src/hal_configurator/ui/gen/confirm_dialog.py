# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/confirm_dialog.ui'
#
# Created: Tue Mar 12 14:31:50 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfirmDialog(object):
    def setupUi(self, ConfirmDialog):
        ConfirmDialog.setObjectName("ConfirmDialog")
        ConfirmDialog.resize(400, 65)
        self.verticalLayout = QtGui.QVBoxLayout(ConfirmDialog)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.la_confirm_message = QtGui.QLabel(ConfirmDialog)
        self.la_confirm_message.setStyleSheet("color:rgb(34, 22, 143)")
        self.la_confirm_message.setObjectName("la_confirm_message")
        self.verticalLayout.addWidget(self.la_confirm_message)
        self.buttons = QtGui.QDialogButtonBox(ConfirmDialog)
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttons.setObjectName("buttons")
        self.verticalLayout.addWidget(self.buttons)

        self.retranslateUi(ConfirmDialog)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL("accepted()"), ConfirmDialog.accept)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL("rejected()"), ConfirmDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfirmDialog)

    def retranslateUi(self, ConfirmDialog):
        ConfirmDialog.setWindowTitle(QtGui.QApplication.translate("ConfirmDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.la_confirm_message.setText(QtGui.QApplication.translate("ConfirmDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">la Text</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

