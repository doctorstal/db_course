# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'one_user.ui'
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

class Ui_executorForm(object):
    def setupUi(self, executorForm):
        executorForm.setObjectName(_fromUtf8("executorForm"))
        executorForm.resize(645, 225)
        self.verticalLayout = QtGui.QVBoxLayout(executorForm)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.userNameButton = QtGui.QPushButton(executorForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userNameButton.sizePolicy().hasHeightForWidth())
        self.userNameButton.setSizePolicy(sizePolicy)
        self.userNameButton.setMinimumSize(QtCore.QSize(350, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/profle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userNameButton.setIcon(icon)
        self.userNameButton.setIconSize(QtCore.QSize(20, 20))
        self.userNameButton.setObjectName(_fromUtf8("userNameButton"))
        self.verticalLayout.addWidget(self.userNameButton)
        self.tasksBox = QtGui.QGroupBox(executorForm)
        self.tasksBox.setObjectName(_fromUtf8("tasksBox"))
        self.verticalLayout.addWidget(self.tasksBox)

        self.retranslateUi(executorForm)
        QtCore.QMetaObject.connectSlotsByName(executorForm)

    def retranslateUi(self, executorForm):
        executorForm.setWindowTitle(_translate("executorForm", "Form", None))
        self.userNameButton.setToolTip(_translate("executorForm", "Expand users data", None))
        self.userNameButton.setStatusTip(_translate("executorForm", "Expand users data", None))
        self.userNameButton.setText(_translate("executorForm", "User name", None))
        self.userNameButton.setShortcut(_translate("executorForm", "Alt+C", None))
        self.tasksBox.setTitle(_translate("executorForm", "Tasks", None))

import res_rc
