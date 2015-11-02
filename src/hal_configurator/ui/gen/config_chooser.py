# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/halicea/projects/hal_automator/utils/qtUi/config_chooser.ui'
#
# Created: Mon Nov  2 11:05:47 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigChooserWidget(object):
    def setupUi(self, ConfigChooserWidget):
        ConfigChooserWidget.setObjectName("ConfigChooserWidget")
        ConfigChooserWidget.resize(134, 68)
        self.btn_open_config = QtGui.QPushButton(ConfigChooserWidget)
        self.btn_open_config.setGeometry(QtCore.QRect(10, 20, 114, 32))
        self.btn_open_config.setObjectName("btn_open_config")

        self.retranslateUi(ConfigChooserWidget)
        QtCore.QMetaObject.connectSlotsByName(ConfigChooserWidget)

    def retranslateUi(self, ConfigChooserWidget):
        ConfigChooserWidget.setWindowTitle(QtGui.QApplication.translate("ConfigChooserWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_open_config.setText(QtGui.QApplication.translate("ConfigChooserWidget", "Open Config", None, QtGui.QApplication.UnicodeUTF8))

