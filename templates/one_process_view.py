# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'one_process_view.ui'
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
        self.showTasksButton = QtGui.QPushButton(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showTasksButton.sizePolicy().hasHeightForWidth())
        self.showTasksButton.setSizePolicy(sizePolicy)
        self.showTasksButton.setMinimumSize(QtCore.QSize(150, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/crossroads.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showTasksButton.setIcon(icon)
        self.showTasksButton.setIconSize(QtCore.QSize(20, 20))
        self.showTasksButton.setObjectName(_fromUtf8("showTasksButton"))
        self.horizontalLayout.addWidget(self.showTasksButton)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.label.setText(_translate("Frame", "Process name", None))
        self.showTasksButton.setToolTip(_translate("Frame", "Show related tasks", None))
        self.showTasksButton.setStatusTip(_translate("Frame", "Show related tasks", None))
        self.showTasksButton.setText(_translate("Frame", "Show tasks", None))

import res_rc
