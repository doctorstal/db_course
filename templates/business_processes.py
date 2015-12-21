# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'business_processes.ui'
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
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.chooseContractButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseContractButton.sizePolicy().hasHeightForWidth())
        self.chooseContractButton.setSizePolicy(sizePolicy)
        self.chooseContractButton.setMinimumSize(QtCore.QSize(250, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/clipboard.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chooseContractButton.setIcon(icon)
        self.chooseContractButton.setIconSize(QtCore.QSize(45, 45))
        self.chooseContractButton.setObjectName(_fromUtf8("chooseContractButton"))
        self.gridLayout.addWidget(self.chooseContractButton, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.processesContainer = QtGui.QScrollArea(Form)
        self.processesContainer.setWidgetResizable(True)
        self.processesContainer.setObjectName(_fromUtf8("processesContainer"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 821, 355))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.processesContainer.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.processesContainer, 1, 0, 1, 3)
        self.addNewProcessButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addNewProcessButton.sizePolicy().hasHeightForWidth())
        self.addNewProcessButton.setSizePolicy(sizePolicy)
        self.addNewProcessButton.setMinimumSize(QtCore.QSize(250, 100))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/merge.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addNewProcessButton.setIcon(icon1)
        self.addNewProcessButton.setIconSize(QtCore.QSize(45, 45))
        self.addNewProcessButton.setObjectName(_fromUtf8("addNewProcessButton"))
        self.gridLayout.addWidget(self.addNewProcessButton, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.chooseContractButton.setToolTip(_translate("Form", "Select another contract (Alt + C)", None))
        self.chooseContractButton.setStatusTip(_translate("Form", "Select another contract (Alt + C)", None))
        self.chooseContractButton.setText(_translate("Form", "Select contract", None))
        self.chooseContractButton.setShortcut(_translate("Form", "Alt+C", None))
        self.label.setText(_translate("Form", "<Contract not selected>", None))
        self.addNewProcessButton.setToolTip(_translate("Form", "Add new process (Alt + P)", None))
        self.addNewProcessButton.setStatusTip(_translate("Form", "Add new process (Alt + P)", None))
        self.addNewProcessButton.setText(_translate("Form", "Add new process", None))
        self.addNewProcessButton.setShortcut(_translate("Form", "Alt+P", None))

import res_rc
