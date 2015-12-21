# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_contract_text.ui'
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

class Ui_editWindow(object):
    def setupUi(self, editWindow):
        editWindow.setObjectName(_fromUtf8("editWindow"))
        editWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(editWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setMinimumSize(QtCore.QSize(250, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/upload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon)
        self.saveButton.setIconSize(QtCore.QSize(45, 45))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.verticalLayout.addWidget(self.saveButton)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        editWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(editWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        editWindow.setStatusBar(self.statusbar)

        self.retranslateUi(editWindow)
        QtCore.QMetaObject.connectSlotsByName(editWindow)

    def retranslateUi(self, editWindow):
        editWindow.setWindowTitle(_translate("editWindow", "Edit Contract Text", None))
        self.saveButton.setToolTip(_translate("editWindow", "Send text to database (Ctrl + S)", None))
        self.saveButton.setStatusTip(_translate("editWindow", "Send text to database (Ctrl + S)", None))
        self.saveButton.setText(_translate("editWindow", "Save text to database", None))
        self.saveButton.setShortcut(_translate("editWindow", "Ctrl+S", None))

import res_rc
