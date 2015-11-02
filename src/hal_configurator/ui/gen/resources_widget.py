# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/halicea/projects/hal_automator/utils/qtUi/resources_widget.ui'
#
# Created: Mon Nov  2 11:05:52 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ResourcesWidget(object):
    def setupUi(self, ResourcesWidget):
        ResourcesWidget.setObjectName("ResourcesWidget")
        ResourcesWidget.resize(295, 687)
        self.verticalLayout = QtGui.QVBoxLayout(ResourcesWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs_vars = QtGui.QTabWidget(ResourcesWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs_vars.sizePolicy().hasHeightForWidth())
        self.tabs_vars.setSizePolicy(sizePolicy)
        self.tabs_vars.setBaseSize(QtCore.QSize(200, 0))
        self.tabs_vars.setObjectName("tabs_vars")
        self.pg_variables = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pg_variables.sizePolicy().hasHeightForWidth())
        self.pg_variables.setSizePolicy(sizePolicy)
        self.pg_variables.setObjectName("pg_variables")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.pg_variables)
        self.verticalLayout_4.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lv_variables = VariablesWindow(self.pg_variables)
        self.lv_variables.setObjectName("lv_variables")
        self.verticalLayout_4.addWidget(self.lv_variables)
        self.tabs_vars.addTab(self.pg_variables, "")
        self.pg_resources = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pg_resources.sizePolicy().hasHeightForWidth())
        self.pg_resources.setSizePolicy(sizePolicy)
        self.pg_resources.setObjectName("pg_resources")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.pg_resources)
        self.verticalLayout_6.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, -1, 0, 10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lv_resources = ResourcesWindow(self.pg_resources)
        self.lv_resources.setObjectName("lv_resources")
        self.verticalLayout_6.addWidget(self.lv_resources)
        self.tabs_vars.addTab(self.pg_resources, "")
        self.verticalLayout.addWidget(self.tabs_vars)

        self.retranslateUi(ResourcesWidget)
        self.tabs_vars.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ResourcesWidget)

    def retranslateUi(self, ResourcesWidget):
        ResourcesWidget.setWindowTitle(QtGui.QApplication.translate("ResourcesWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs_vars.setTabText(self.tabs_vars.indexOf(self.pg_variables), QtGui.QApplication.translate("ResourcesWidget", "Variables", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs_vars.setTabToolTip(self.tabs_vars.indexOf(self.pg_variables), QtGui.QApplication.translate("ResourcesWidget", "List of available variables", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs_vars.setTabText(self.tabs_vars.indexOf(self.pg_resources), QtGui.QApplication.translate("ResourcesWidget", "Resources", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs_vars.setTabToolTip(self.tabs_vars.indexOf(self.pg_resources), QtGui.QApplication.translate("ResourcesWidget", "List of available resources", None, QtGui.QApplication.UnicodeUTF8))

from hal_configurator.ui.resourceswindow import ResourcesWindow
from hal_configurator.ui.variableswindow import VariablesWindow
