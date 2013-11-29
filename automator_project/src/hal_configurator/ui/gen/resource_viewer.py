# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/resource_viewer.ui'
#
# Created: Thu Nov 28 22:51:09 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ResourceViewer(object):
    def setupUi(self, ResourceViewer):
        ResourceViewer.setObjectName("ResourceViewer")
        ResourceViewer.resize(128, 155)
        self.gridLayout = QtGui.QGridLayout(ResourceViewer)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.webView = QtWebKit.QWebView(ResourceViewer)
        self.webView.setAutoFillBackground(True)
        self.webView.setUrl(QtCore.QUrl("qrc:/buttons/images/HAL-9000-icon.png"))
        self.webView.setObjectName("webView")
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)

        self.retranslateUi(ResourceViewer)
        QtCore.QMetaObject.connectSlotsByName(ResourceViewer)

    def retranslateUi(self, ResourceViewer):
        ResourceViewer.setWindowTitle(QtGui.QApplication.translate("ResourceViewer", "Form", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
