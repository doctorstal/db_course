# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'one_task_view.ui'
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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(717, 70)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.status = QtGui.QLabel(Frame)
        self.status.setObjectName(_fromUtf8("status"))
        self.horizontalLayout.addWidget(self.status)
        self.changeExecutorButton = QtGui.QPushButton(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changeExecutorButton.sizePolicy().hasHeightForWidth())
        self.changeExecutorButton.setSizePolicy(sizePolicy)
        self.changeExecutorButton.setMinimumSize(QtCore.QSize(150, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/contacts.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeExecutorButton.setIcon(icon)
        self.changeExecutorButton.setIconSize(QtCore.QSize(20, 20))
        self.changeExecutorButton.setObjectName(_fromUtf8("changeExecutorButton"))
        self.horizontalLayout.addWidget(self.changeExecutorButton)
        self.proceedStatusButton = QtGui.QPushButton(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proceedStatusButton.sizePolicy().hasHeightForWidth())
        self.proceedStatusButton.setSizePolicy(sizePolicy)
        self.proceedStatusButton.setMinimumSize(QtCore.QSize(150, 50))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/arrow-up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.proceedStatusButton.setIcon(icon1)
        self.proceedStatusButton.setIconSize(QtCore.QSize(20, 20))
        self.proceedStatusButton.setObjectName(_fromUtf8("proceedStatusButton"))
        self.horizontalLayout.addWidget(self.proceedStatusButton)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.label.setText(_translate("Frame", "Task name", None))
        self.status.setText(_translate("Frame", "Task status", None))
        self.changeExecutorButton.setToolTip(_translate("Frame", "Change executor", None))
        self.changeExecutorButton.setStatusTip(_translate("Frame", "Change executor", None))
        self.changeExecutorButton.setText(_translate("Frame", "Change executor", None))
        self.proceedStatusButton.setToolTip(_translate("Frame", "Assign next status to task", None))
        self.proceedStatusButton.setStatusTip(_translate("Frame", "Assign next status to task", None))
        self.proceedStatusButton.setText(_translate("Frame", "Proceed status", None))

import res_rc
