# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/halicea/projects/hal_automator/utils/qtUi/resources_widget.ui'
#
# Created: Mon Nov  2 04:54:55 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ResourcesWidget(object):
    def setupUi(self, ResourcesWidget):
        ResourcesWidget.setObjectName("ResourcesWidget")
        ResourcesWidget.resize(295, 687)
        self.horizontalLayout = QtGui.QHBoxLayout(ResourcesWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabs_vars = QtGui.QTabWidget(ResourcesWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs_vars.sizePolicy().hasHeightForWidth())
        self.tabs_vars.setSizePolicy(sizePolicy)
        self.tabs_vars.setBaseSize(QtCore.QSize(200, 0))
        self.tabs_vars.setObjectName("tabs_vars")
        self.tab_variables = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_variables.sizePolicy().hasHeightForWidth())
        self.tab_variables.setSizePolicy(sizePolicy)
        self.tab_variables.setObjectName("tab_variables")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_variables)
        self.verticalLayout_4.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lv_vars = DragableList(self.tab_variables)
        self.lv_vars.setDragEnabled(True)
        self.lv_vars.setAlternatingRowColors(True)
        self.lv_vars.setObjectName("lv_vars")
        self.verticalLayout_4.addWidget(self.lv_vars)
        self.search_vars = QtGui.QLineEdit(self.tab_variables)
        self.search_vars.setObjectName("search_vars")
        self.verticalLayout_4.addWidget(self.search_vars)
        self.tabs_vars.addTab(self.tab_variables, "")
        self.tab_resources = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_resources.sizePolicy().hasHeightForWidth())
        self.tab_resources.setSizePolicy(sizePolicy)
        self.tab_resources.setObjectName("tab_resources")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_resources)
        self.verticalLayout_6.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_6.setContentsMargins(0, -1, 0, 10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lv_resources = ResourcesList(self.tab_resources)
        self.lv_resources.setObjectName("lv_resources")
        self.verticalLayout_6.addWidget(self.lv_resources)
        self.search_resources = QtGui.QLineEdit(self.tab_resources)
        self.search_resources.setObjectName("search_resources")
        self.verticalLayout_6.addWidget(self.search_resources)
        self.tabs_vars.addTab(self.tab_resources, "")
        self.horizontalLayout.addWidget(self.tabs_vars)

        self.retranslateUi(ResourcesWidget)
        self.tabs_vars.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ResourcesWidget)

    def retranslateUi(self, ResourcesWidget):
        ResourcesWidget.setWindowTitle(QtGui.QApplication.translate("ResourcesWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.search_vars.setPlaceholderText(QtGui.QApplication.translate("ResourcesWidget", "Search ...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs_vars.setTabText(self.tabs_vars.indexOf(self.tab_variables), QtGui.QApplication.translate("ResourcesWidget", "Variables", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs_vars.setTabToolTip(self.tabs_vars.indexOf(self.tab_variables), QtGui.QApplication.translate("ResourcesWidget", "List of available variables", None, QtGui.QApplication.UnicodeUTF8))
        self.search_resources.setPlaceholderText(QtGui.QApplication.translate("ResourcesWidget", "Search ...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs_vars.setTabText(self.tabs_vars.indexOf(self.tab_resources), QtGui.QApplication.translate("ResourcesWidget", "Resources", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs_vars.setTabToolTip(self.tabs_vars.indexOf(self.tab_resources), QtGui.QApplication.translate("ResourcesWidget", "List of available resources", None, QtGui.QApplication.UnicodeUTF8))

from hal_configurator.ui.custom_widgets.resources_list import ResourcesList
from hal_configurator.ui.custom_widgets.dragable_list import DragableList
