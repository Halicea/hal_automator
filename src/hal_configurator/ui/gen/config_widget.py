# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/halicea/projects/hal_automator/utils/qtUi/config_widget.ui'
#
# Created: Mon Nov  2 11:05:49 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigForm(object):
    def setupUi(self, ConfigForm):
        ConfigForm.setObjectName("ConfigForm")
        ConfigForm.resize(1022, 642)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfigForm.sizePolicy().hasHeightForWidth())
        ConfigForm.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(ConfigForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_name = QtGui.QLineEdit(ConfigForm)
        self.txt_name.setObjectName("txt_name")
        self.horizontalLayout.addWidget(self.txt_name)
        self.btn_save = QtGui.QPushButton(ConfigForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tlbx_bundles = QtGui.QToolBox(ConfigForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tlbx_bundles.sizePolicy().hasHeightForWidth())
        self.tlbx_bundles.setSizePolicy(sizePolicy)
        self.tlbx_bundles.setBaseSize(QtCore.QSize(0, 0))
        self.tlbx_bundles.setObjectName("tlbx_bundles")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 998, 507))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setObjectName("page")
        self.tlbx_bundles.addItem(self.page, "")
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 16, 507))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy)
        self.page_2.setObjectName("page_2")
        self.tlbx_bundles.addItem(self.page_2, "")
        self.verticalLayout.addWidget(self.tlbx_bundles)

        self.retranslateUi(ConfigForm)
        self.tlbx_bundles.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ConfigForm)

    def retranslateUi(self, ConfigForm):
        ConfigForm.setWindowTitle(QtGui.QApplication.translate("ConfigForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_save.setText(QtGui.QApplication.translate("ConfigForm", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.tlbx_bundles.setItemText(self.tlbx_bundles.indexOf(self.page), QtGui.QApplication.translate("ConfigForm", "Page 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tlbx_bundles.setItemText(self.tlbx_bundles.indexOf(self.page_2), QtGui.QApplication.translate("ConfigForm", "Page 2", None, QtGui.QApplication.UnicodeUTF8))

