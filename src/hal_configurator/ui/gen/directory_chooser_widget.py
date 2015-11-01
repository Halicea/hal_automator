# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/halicea/projects/hal_automator/utils/qtUi/shared/directory_chooser_widget.ui'
#
# Created: Sun Nov  1 22:25:37 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DirectoryChooserWidget(object):
    def setupUi(self, DirectoryChooserWidget):
        DirectoryChooserWidget.setObjectName("DirectoryChooserWidget")
        DirectoryChooserWidget.resize(375, 32)
        self.horizontalLayout = QtGui.QHBoxLayout(DirectoryChooserWidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_dir = QtGui.QLineEdit(DirectoryChooserWidget)
        self.txt_dir.setObjectName("txt_dir")
        self.horizontalLayout.addWidget(self.txt_dir)
        self.btn_browse = QtGui.QToolButton(DirectoryChooserWidget)
        self.btn_browse.setObjectName("btn_browse")
        self.horizontalLayout.addWidget(self.btn_browse)
        self.btn_remove = QtGui.QToolButton(DirectoryChooserWidget)
        self.btn_remove.setObjectName("btn_remove")
        self.horizontalLayout.addWidget(self.btn_remove)

        self.retranslateUi(DirectoryChooserWidget)
        QtCore.QMetaObject.connectSlotsByName(DirectoryChooserWidget)

    def retranslateUi(self, DirectoryChooserWidget):
        DirectoryChooserWidget.setWindowTitle(QtGui.QApplication.translate("DirectoryChooserWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_browse.setText(QtGui.QApplication.translate("DirectoryChooserWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_remove.setText(QtGui.QApplication.translate("DirectoryChooserWidget", "X", None, QtGui.QApplication.UnicodeUTF8))

