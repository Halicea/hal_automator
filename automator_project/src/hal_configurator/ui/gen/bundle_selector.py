# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/bundle_selector.ui'
#
# Created: Thu Nov 28 03:52:24 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_bundle_selector(object):
    def setupUi(self, bundle_selector):
        bundle_selector.setObjectName("bundle_selector")
        bundle_selector.resize(480, 640)
        bundle_selector.setTitle("")
        bundle_selector.setFlat(True)
        bundle_selector.setCheckable(False)
        self.verticalLayout = QtGui.QVBoxLayout(bundle_selector)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbTogleAll = QtGui.QCheckBox(bundle_selector)
        self.cbTogleAll.setChecked(True)
        self.cbTogleAll.setObjectName("cbTogleAll")
        self.verticalLayout.addWidget(self.cbTogleAll)
        self.lvBundles = QtGui.QListView(bundle_selector)
        self.lvBundles.setObjectName("lvBundles")
        self.verticalLayout.addWidget(self.lvBundles)
        self.btnSave = QtGui.QPushButton(bundle_selector)
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout.addWidget(self.btnSave)

        self.retranslateUi(bundle_selector)
        QtCore.QMetaObject.connectSlotsByName(bundle_selector)

    def retranslateUi(self, bundle_selector):
        bundle_selector.setWindowTitle(QtGui.QApplication.translate("bundle_selector", "Select Bundles", None, QtGui.QApplication.UnicodeUTF8))
        self.cbTogleAll.setText(QtGui.QApplication.translate("bundle_selector", "Select/Deselect All", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("bundle_selector", "Save", None, QtGui.QApplication.UnicodeUTF8))

