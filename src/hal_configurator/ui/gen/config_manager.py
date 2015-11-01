# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/halicea/projects/hal_automator/utils/qtUi/config_manager.ui'
#
# Created: Sun Nov  1 19:09:17 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigManager(object):
    def setupUi(self, ConfigManager):
        ConfigManager.setObjectName("ConfigManager")
        ConfigManager.resize(332, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttons/images/HAL-9000-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConfigManager.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(ConfigManager)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        ConfigManager.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 332, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRecent = QtGui.QMenu(self.menuFile)
        self.menuRecent.setObjectName("menuRecent")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        ConfigManager.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ConfigManager)
        self.statusbar.setObjectName("statusbar")
        ConfigManager.setStatusBar(self.statusbar)
        self.actionPreferences = QtGui.QAction(ConfigManager)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFile.addAction(self.menuRecent.menuAction())
        self.menuFile.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(ConfigManager)
        QtCore.QMetaObject.connectSlotsByName(ConfigManager)

    def retranslateUi(self, ConfigManager):
        ConfigManager.setWindowTitle(QtGui.QApplication.translate("ConfigManager", "Configuration Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ConfigManager", "Choose Configuration:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("ConfigManager", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRecent.setTitle(QtGui.QApplication.translate("ConfigManager", "Recent", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("ConfigManager", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("ConfigManager", "Preferences", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
