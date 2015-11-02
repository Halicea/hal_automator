# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/halicea/projects/hal_automator/utils/qtUi/config_bundle.ui'
#
# Created: Mon Nov  2 11:05:47 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BundleWidget(object):
    def setupUi(self, BundleWidget):
        BundleWidget.setObjectName("BundleWidget")
        BundleWidget.resize(665, 526)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BundleWidget.sizePolicy().hasHeightForWidth())
        BundleWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(BundleWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(10, 0, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scroll_area = QtGui.QScrollArea(BundleWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_area.sizePolicy().hasHeightForWidth())
        self.scroll_area.setSizePolicy(sizePolicy)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scroll_contents = QtGui.QWidget()
        self.scroll_contents.setGeometry(QtCore.QRect(0, 0, 643, 514))
        self.scroll_contents.setObjectName("scroll_contents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scroll_contents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.contents = ContentFrame(self.scroll_contents)
        self.contents.setStyleSheet("")
        self.contents.setFrameShape(QtGui.QFrame.NoFrame)
        self.contents.setFrameShadow(QtGui.QFrame.Raised)
        self.contents.setLineWidth(0)
        self.contents.setObjectName("contents")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.contents)
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_3.setContentsMargins(0, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addWidget(self.contents)
        self.scroll_area.setWidget(self.scroll_contents)
        self.verticalLayout.addWidget(self.scroll_area)

        self.retranslateUi(BundleWidget)
        QtCore.QMetaObject.connectSlotsByName(BundleWidget)

    def retranslateUi(self, BundleWidget):
        BundleWidget.setWindowTitle(QtGui.QApplication.translate("BundleWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

from content_frame import ContentFrame
