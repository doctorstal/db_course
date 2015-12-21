# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'companies_contracts.ui'
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
        Form.resize(841, 481)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addCompanyButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addCompanyButton.sizePolicy().hasHeightForWidth())
        self.addCompanyButton.setSizePolicy(sizePolicy)
        self.addCompanyButton.setMinimumSize(QtCore.QSize(250, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/blimp.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addCompanyButton.setIcon(icon)
        self.addCompanyButton.setIconSize(QtCore.QSize(45, 45))
        self.addCompanyButton.setObjectName(_fromUtf8("addCompanyButton"))
        self.verticalLayout.addWidget(self.addCompanyButton)
        self.companiesContainer = QtGui.QScrollArea(Form)
        self.companiesContainer.setWidgetResizable(True)
        self.companiesContainer.setObjectName(_fromUtf8("companiesContainer"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 821, 355))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.companiesContainer.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.companiesContainer)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.addCompanyButton.setToolTip(_translate("Form", "Add new company you have a contracts with (Alt + C)", None))
        self.addCompanyButton.setStatusTip(_translate("Form", "Add new company you have a contracts with (Alt + C)", None))
        self.addCompanyButton.setText(_translate("Form", "Add new company", None))
        self.addCompanyButton.setShortcut(_translate("Form", "Alt+C", None))

import res_rc
