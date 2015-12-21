# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionLogout = QtGui.QAction(MainWindow)
        self.actionLogout.setObjectName(_fromUtf8("actionLogout"))
        self.actionReport = QtGui.QAction(MainWindow)
        self.actionReport.setObjectName(_fromUtf8("actionReport"))
        self.action_5 = QtGui.QAction(MainWindow)
        self.action_5.setObjectName(_fromUtf8("action_5"))
        self.action_6 = QtGui.QAction(MainWindow)
        self.action_6.setObjectName(_fromUtf8("action_6"))
        self.actionCreateExecutor = QtGui.QAction(MainWindow)
        self.actionCreateExecutor.setObjectName(_fromUtf8("actionCreateExecutor"))
        self.actionCreateCompany = QtGui.QAction(MainWindow)
        self.actionCreateCompany.setObjectName(_fromUtf8("actionCreateCompany"))
        self.actionCreateContract = QtGui.QAction(MainWindow)
        self.actionCreateContract.setObjectName(_fromUtf8("actionCreateContract"))
        self.menu.addAction(self.actionReport)
        self.menu.addAction(self.actionLogout)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menu_2.addAction(self.actionCreateExecutor)
        self.menu_2.addAction(self.actionCreateCompany)
        self.menu_2.addAction(self.actionCreateContract)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menu.setTitle(_translate("MainWindow", "Програма", None))
        self.menu_2.setTitle(_translate("MainWindow", "Створити", None))
        self.actionExit.setText(_translate("MainWindow", "Вихід", None))
        self.actionLogout.setText(_translate("MainWindow", "Завершити сеанс", None))
        self.actionReport.setText(_translate("MainWindow", "Генерувати звіт", None))
        self.action_5.setText(_translate("MainWindow", "Договір", None))
        self.action_6.setText(_translate("MainWindow", "Подію", None))
        self.actionCreateExecutor.setText(_translate("MainWindow", "Виконавця", None))
        self.actionCreateCompany.setText(_translate("MainWindow", "Компанію", None))
        self.actionCreateContract.setText(_translate("MainWindow", "Договір", None))

