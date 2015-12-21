# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasks.ui'
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
        self.chooseProcessButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseProcessButton.sizePolicy().hasHeightForWidth())
        self.chooseProcessButton.setSizePolicy(sizePolicy)
        self.chooseProcessButton.setMinimumSize(QtCore.QSize(250, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/merge.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chooseProcessButton.setIcon(icon)
        self.chooseProcessButton.setIconSize(QtCore.QSize(45, 45))
        self.chooseProcessButton.setObjectName(_fromUtf8("chooseProcessButton"))
        self.gridLayout.addWidget(self.chooseProcessButton, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tasksContainer = QtGui.QScrollArea(Form)
        self.tasksContainer.setWidgetResizable(True)
        self.tasksContainer.setObjectName(_fromUtf8("tasksContainer"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 821, 355))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.tasksContainer.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.tasksContainer, 1, 0, 1, 3)
        self.addNewTaskButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addNewTaskButton.sizePolicy().hasHeightForWidth())
        self.addNewTaskButton.setSizePolicy(sizePolicy)
        self.addNewTaskButton.setMinimumSize(QtCore.QSize(250, 100))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/crossroads.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addNewTaskButton.setIcon(icon1)
        self.addNewTaskButton.setIconSize(QtCore.QSize(45, 45))
        self.addNewTaskButton.setObjectName(_fromUtf8("addNewTaskButton"))
        self.gridLayout.addWidget(self.addNewTaskButton, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.chooseProcessButton.setToolTip(_translate("Form", "Choose other process (Alt+P)", None))
        self.chooseProcessButton.setStatusTip(_translate("Form", "Choose other process (Alt + P)", None))
        self.chooseProcessButton.setText(_translate("Form", "Choose process", None))
        self.chooseProcessButton.setShortcut(_translate("Form", "Alt+P", None))
        self.label.setText(_translate("Form", "<Process not selected>", None))
        self.addNewTaskButton.setToolTip(_translate("Form", "Add new task(Alt + T)", None))
        self.addNewTaskButton.setStatusTip(_translate("Form", "Add new task(Alt + T)", None))
        self.addNewTaskButton.setText(_translate("Form", "Add new task", None))
        self.addNewTaskButton.setShortcut(_translate("Form", "Alt+T", None))

import res_rc
