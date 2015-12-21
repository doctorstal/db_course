# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startscreen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(882, 533)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(540, 340))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.tasksButton = QtGui.QPushButton(self.widget)
        self.tasksButton.setGeometry(QtCore.QRect(270, 120, 250, 100))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tasksButton.sizePolicy().hasHeightForWidth())
        self.tasksButton.setSizePolicy(sizePolicy)
        self.tasksButton.setMinimumSize(QtCore.QSize(250, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/crossroads.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tasksButton.setIcon(icon)
        self.tasksButton.setIconSize(QtCore.QSize(45, 45))
        self.tasksButton.setObjectName(_fromUtf8("tasksButton"))
        self.reportButton = QtGui.QPushButton(self.widget)
        self.reportButton.setGeometry(QtCore.QRect(15, 225, 505, 100))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reportButton.sizePolicy().hasHeightForWidth())
        self.reportButton.setSizePolicy(sizePolicy)
        self.reportButton.setMinimumSize(QtCore.QSize(505, 100))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/trends.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reportButton.setIcon(icon1)
        self.reportButton.setIconSize(QtCore.QSize(45, 45))
        self.reportButton.setObjectName(_fromUtf8("reportButton"))
        self.processesButton = QtGui.QPushButton(self.widget)
        self.processesButton.setGeometry(QtCore.QRect(270, 15, 250, 100))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processesButton.sizePolicy().hasHeightForWidth())
        self.processesButton.setSizePolicy(sizePolicy)
        self.processesButton.setMinimumSize(QtCore.QSize(250, 100))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/merge.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.processesButton.setIcon(icon2)
        self.processesButton.setIconSize(QtCore.QSize(45, 45))
        self.processesButton.setObjectName(_fromUtf8("processesButton"))
        self.responsiblesButton = QtGui.QPushButton(self.widget)
        self.responsiblesButton.setGeometry(QtCore.QRect(15, 120, 250, 100))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.responsiblesButton.sizePolicy().hasHeightForWidth())
        self.responsiblesButton.setSizePolicy(sizePolicy)
        self.responsiblesButton.setMinimumSize(QtCore.QSize(250, 100))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/contacts.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.responsiblesButton.setIcon(icon3)
        self.responsiblesButton.setIconSize(QtCore.QSize(45, 45))
        self.responsiblesButton.setObjectName(_fromUtf8("responsiblesButton"))
        self.companiesButton = QtGui.QPushButton(self.widget)
        self.companiesButton.setGeometry(QtCore.QRect(15, 15, 250, 100))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.companiesButton.sizePolicy().hasHeightForWidth())
        self.companiesButton.setSizePolicy(sizePolicy)
        self.companiesButton.setMinimumSize(QtCore.QSize(250, 100))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/briefcase.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.companiesButton.setIcon(icon4)
        self.companiesButton.setIconSize(QtCore.QSize(45, 45))
        self.companiesButton.setObjectName(_fromUtf8("companiesButton"))
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.tasksButton.setToolTip(_translate("Form", "Change tasks statuses and responsibles (Alt + T)", None))
        self.tasksButton.setStatusTip(_translate("Form", "Change tasks statuses and responsibles (Alt + T)", None))
        self.tasksButton.setText(_translate("Form", "Tasks", None))
        self.tasksButton.setShortcut(_translate("Form", "Alt+T", None))
        self.reportButton.setToolTip(_translate("Form", "Is it Monday already? You should defenitely print this!", None))
        self.reportButton.setStatusTip(_translate("Form", "Is it Monday already? You should defenitely print this!", None))
        self.reportButton.setText(_translate("Form", "Generate report", None))
        self.reportButton.setShortcut(_translate("Form", "Alt+G", None))
        self.processesButton.setToolTip(_translate("Form", "Create business process (Alt+B)", None))
        self.processesButton.setStatusTip(_translate("Form", "Create business process (Alt + B)", None))
        self.processesButton.setText(_translate("Form", "Business processes", None))
        self.processesButton.setShortcut(_translate("Form", "Alt+B", None))
        self.responsiblesButton.setToolTip(_translate("Form", "Add/Remove task executors (Alt + R)", None))
        self.responsiblesButton.setStatusTip(_translate("Form", "Add/Remove task executors", None))
        self.responsiblesButton.setText(_translate("Form", "Responsibles", None))
        self.responsiblesButton.setShortcut(_translate("Form", "Alt+R", None))
        self.companiesButton.setToolTip(_translate("Form", "Add/remove companies and contracts (Alt+C)", None))
        self.companiesButton.setStatusTip(_translate("Form", "Add/remove companies and contracts (Alt+C)", None))
        self.companiesButton.setText(_translate("Form", "Companies/contracts", None))
        self.companiesButton.setShortcut(_translate("Form", "Alt+C", None))

import res_rc
