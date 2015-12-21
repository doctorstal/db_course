# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'one_company_view.ui'
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

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName(_fromUtf8("GroupBox"))
        GroupBox.resize(817, 287)
        self.verticalLayout = QtGui.QVBoxLayout(GroupBox)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addContractButton = QtGui.QPushButton(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addContractButton.sizePolicy().hasHeightForWidth())
        self.addContractButton.setSizePolicy(sizePolicy)
        self.addContractButton.setMinimumSize(QtCore.QSize(150, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/color/clipboard.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addContractButton.setIcon(icon)
        self.addContractButton.setIconSize(QtCore.QSize(20, 20))
        self.addContractButton.setObjectName(_fromUtf8("addContractButton"))
        self.horizontalLayout.addWidget(self.addContractButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.collapseButton = QtGui.QToolButton(GroupBox)
        self.collapseButton.setMinimumSize(QtCore.QSize(20, 0))
        self.collapseButton.setIconSize(QtCore.QSize(12, 10))
        self.collapseButton.setCheckable(True)
        self.collapseButton.setChecked(False)
        self.collapseButton.setArrowType(QtCore.Qt.UpArrow)
        self.collapseButton.setObjectName(_fromUtf8("collapseButton"))
        self.horizontalLayout.addWidget(self.collapseButton, QtCore.Qt.AlignBottom)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.contractsContainer = QtGui.QWidget(GroupBox)
        self.contractsContainer.setObjectName(_fromUtf8("contractsContainer"))
        self.verticalLayout.addWidget(self.contractsContainer)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox", None))
        GroupBox.setTitle(_translate("GroupBox", "GroupBox", None))
        self.addContractButton.setToolTip(_translate("GroupBox", "Add new contract to this company", None))
        self.addContractButton.setStatusTip(_translate("GroupBox", "Add new company to this company", None))
        self.addContractButton.setText(_translate("GroupBox", "Add new contract", None))
        self.addContractButton.setShortcut(_translate("GroupBox", "Alt+C", None))
        self.collapseButton.setToolTip(_translate("GroupBox", "Expand/Collapse contracts", None))
        self.collapseButton.setStatusTip(_translate("GroupBox", "Expand/Collapse contracts", None))
        self.collapseButton.setText(_translate("GroupBox", "...", None))

import res_rc
