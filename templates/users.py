# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'users.ui'
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

class Ui_Executors(object):
    def setupUi(self, Executors):
        Executors.setObjectName(_fromUtf8("Executors"))
        Executors.resize(702, 670)
        self.centralwidget = QtGui.QWidget(Executors)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addNewUserButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addNewUserButton.sizePolicy().hasHeightForWidth())
        self.addNewUserButton.setSizePolicy(sizePolicy)
        self.addNewUserButton.setMinimumSize(QtCore.QSize(250, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/contacts.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addNewUserButton.setIcon(icon)
        self.addNewUserButton.setIconSize(QtCore.QSize(45, 45))
        self.addNewUserButton.setObjectName(_fromUtf8("addNewUserButton"))
        self.verticalLayout.addWidget(self.addNewUserButton, QtCore.Qt.AlignRight)
        self.executorsContainer = QtGui.QScrollArea(self.centralwidget)
        self.executorsContainer.setWidgetResizable(True)
        self.executorsContainer.setObjectName(_fromUtf8("executorsContainer"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 682, 524))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.executorsContainer.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.executorsContainer)
        Executors.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Executors)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Executors.setStatusBar(self.statusbar)

        self.retranslateUi(Executors)
        QtCore.QMetaObject.connectSlotsByName(Executors)

    def retranslateUi(self, Executors):
        Executors.setWindowTitle(_translate("Executors", "MainWindow", None))
        self.addNewUserButton.setToolTip(_translate("Executors", "Add new executor (Ctrl + E)", None))
        self.addNewUserButton.setStatusTip(_translate("Executors", "Add new executor(Ctrl + E)", None))
        self.addNewUserButton.setText(_translate("Executors", "Add new executor", None))
        self.addNewUserButton.setShortcut(_translate("Executors", "Ctrl+P", None))

import res_rc
