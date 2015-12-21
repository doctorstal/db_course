# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 00:35:33 2015

@author: alexeyst
"""

import sys

from PyQt4.QtGui import *

from database import ProductsDB
from templates import enter_text_dlg
from templates import select_dlg
from templates.main_window import Ui_MainWindow


class ReportsApp(QMainWindow):
	'Main class for reports. It will create windows and stuff, you know.'
	ui = Ui_MainWindow()

	def __init__(self):
		super(ReportsApp, self).__init__()
		self.db = ProductsDB()
		self.db.connect("localhost:1521", "sql_developer", "Can_I_have_a_cookie");
		self.initUI()
		self.show()

	def initUI(self):
		'Init template'

		self.ui.setupUi(self)
		self.initMenubarActions()
		self.initTabs()

	def initTabs(self):
		self.usersTable = ExecutorsTableView(self.db)
		self.ui.tabWidget.addTab(self.usersTable, 'Executors')
		self.usersTable.pressed.connect(self.usersTableClicked)

		self.companiesTable = CompaniesTableView(self.db)
		self.ui.tabWidget.addTab(self.companiesTable, 'Companies')

		self.contractsTable = CompaniesContractsView(self.db)
		self.ui.tabWidget.addTab(self.contractsTable, 'Contracts')

		self.processesTable = ProcessesView(self.db)
		self.ui.tabWidget.addTab(self.processesTable, 'Business Processes')

		self.tasksTable = TasksView(self.db)
		self.ui.tabWidget.addTab(self.tasksTable, 'Tasks')

	def usersTableClicked(self):
		print('Clicked'+str(self.usersTable.currentIndex()))
		self.usersTable.selectRow(self.usersTable.currentIndex().row())


	def initMenubarActions(self):
		self.ui.actionExit.triggered.connect(self.doExit)
		self.ui.actionExecutor.triggered.connect(self.createExecutor)
		self.ui.actionCompany.triggered.connect(self.createCompany)

	def createExecutor(self):
		'Create new executor'
		dlg = QDialog()
		dlgUi = enter_text_dlg.Ui_Dialog()
		dlgUi.setupUi(dlg)
		dlgUi.label.setText('Enter executors name:')

		dlg.exec_()

		if(dlgUi.lineEdit.text()!='' and dlg.accepted):
			if(self.db.createNewExecutor(dlgUi.lineEdit.text())):
				self.usersTable.updateTable()
				QMessageBox.information(self, 'Created', 'User successfuly created!')
			else:
				QMessageBox.warning(self, 'Failed', 'Failed to create user.')
	def createCompany(self):
		'Create new company'
		dlg = QDialog()
		dlgUi = enter_text_dlg.Ui_Dialog()
		dlgUi.setupUi(dlg)
		dlgUi.label.setText('Enter company name:')

		dlg.exec_()

		if(dlgUi.lineEdit.text()!='' and dlg.accepted):
			if(self.db.createNewCompany(dlgUi.lineEdit.text())):
				self.companiesTable.updateTable()
				QMessageBox.information(self, 'Created', 'Company successfuly created!')
			else:
				QMessageBox.warning(self, 'Failed', 'Failed to create company.')
	def addContract(self, company_id):
		'Create new company'
		dlg = QDialog()
		dlgUi = enter_text_dlg.Ui_Dialog()
		dlgUi.setupUi(dlg)
		dlgUi.label.setText('Enter contract short description:')

		dlg.exec_()

		if(dlgUi.lineEdit.text()!='' and dlg.accepted):
			if(self.db.createNewContract(company_id, dlgUi.lineEdit.text())):
				self.contractsTable.updateTable()
				QMessageBox.information(self, 'Created', 'Contract successfuly created!')
			else:
				QMessageBox.warning(self, 'Failed', 'Failed to create contract.')

	def addBusinessProcess(self, contract_id):
		'Create new process'
		dlg = QDialog()
		dlgUi = enter_text_dlg.Ui_Dialog()
		dlgUi.setupUi(dlg)
		dlgUi.label.setText('Enter process name:')

		dlg.exec_()

		if(dlgUi.lineEdit.text()!='' and dlg.accepted):
			if(self.db.createNewProcess(contract_id, dlgUi.lineEdit.text())):
				self.processesTable.updateTable()
				QMessageBox.information(self, 'Created', 'Process successfuly created!')
			else:
				QMessageBox.warning(self, 'Failed', 'Failed to create process.')

	def addTask(self, process_id):
		'Create new task'

		dlg = QDialog()
		selectDlgUi = select_dlg.Ui_Dialog()
		selectDlgUi.setupUi(dlg)
		table = self.db.getTable('executors')
		user_ids = []
		for rowid in range(table.rowCount()):
			record = table.record(rowid)
			selectDlgUi.comboBox.addItem(record.value('executor_name'))
			user_ids.append(record.value('executor_id'))

		selectDlgUi.label.setText('Select employee:')

		dlg.exec_()
		user_id = user_ids[selectDlgUi.comboBox.currentIndex()];

		dlg = QDialog()
		dlgUi = enter_text_dlg.Ui_Dialog()
		dlgUi.setupUi(dlg)
		dlgUi.label.setText('Enter task name:')

		dlg.exec_()

		if(dlgUi.lineEdit.text()!='' and dlg.accepted):
			if(self.db.createNewTask(process_id,
									 dlgUi.lineEdit.text(),
									user_id)):
				self.processesTable.updateTable()
				QMessageBox.information(self, 'Created', 'Task successfuly created!')
			else:
				QMessageBox.warning(self, 'Failed', 'Failed to create task.')

	def doExit(self):
		self.close()

class RTableView(QTableView):
	'Table representation'
	def __init__(self, tableModel):
		super(RTableView, self).__init__()
		self.tableModel = tableModel
		self.setModel(tableModel)
		self.horizontalHeader().setResizeMode(QHeaderView.Stretch)
	def updateTable(self):
		self.tableModel.select()

class ExecutorsTableView(RTableView):
	'Table of executors'
	def __init__(self, db):
		executorsTable = db.getTable('executor_list')
		super(ExecutorsTableView, self).__init__(executorsTable)


class CompaniesTableView(QScrollArea):
	'Tab view For companies'
	def __init__(self, db):
		super(CompaniesTableView, self).__init__()
		self.db = db
		self.executorsTable = db.getTable('companies')
		self.setLayout(QVBoxLayout())
		self.initUi()
	def initUi(self):
		'Initialize the ui'
		self.companies = []
		for irow in range(self.executorsTable.rowCount()):
			newCompany = CompanyItem(self.executorsTable.record(irow))
			self.layout().addWidget(newCompany)
			self.companies.append(newCompany)

	def clear(self):
		'Clear contents'
		for company in self.companies:
			company.setParent(None)
		self.companies = []

	def updateTable(self):
		'update table contents from db'
		self.executorsTable.select()
		self.clear()
		self.initUi()

class CompanyItem(QWidget):
	'Displays company and allows to create contracts for it'
	def __init__(self, record):
		"""
		:param record QSqlRecord:
		:return:
		"""
		super(CompanyItem, self).__init__()
		self.record = record
		self.setLayout(QHBoxLayout())
		self.initUi()
	def initUi(self):
		label = QLabel()
		label.setText(self.record.value('company_name').toString())
		self.layout().addWidget(label)
		contractButton = QPushButton()
		contractButton.setText('Add contract')
		self.layout().addWidget(contractButton)
		contractButton.clicked.connect(self.contractButtonClicked)

		showButton = QPushButton()
		showButton.setText('Show details')
#        self.layout().addWidget(showButton)
		showButton.clicked.connect(self.showBtnClicked)
	def showBtnClicked(self):
		mainAppWindow.showCompanyDetails(self.record.value('company_id'))
	def contractButtonClicked(self):
		mainAppWindow.addContract(self.record.value('company_id'))

class CompaniesContractsView(RTableView):
	'Table of contracts'
	def __init__(self, db):
		self.contractsTable = db.getTable('contracts_list')

		super(CompaniesContractsView, self).__init__(self.contractsTable)
		self.initUi()
	def initUi(self):
		self.setColumnHidden(0, True)
		self.verticalHeader().setClickable(True)
		self.verticalHeader().sectionPressed.connect(self.addBusinessProcess)
	def addBusinessProcess(self, index):
		mainAppWindow.addBusinessProcess(self.contractsTable.record(index).value('contract_id'))

class ProcessesView(RTableView):
	'Table of business processes'
	def __init__(self, db):
		self.table = db.getTable('processes_list')
		super(ProcessesView, self).__init__(self.table)
		self.initUi()

	def initUi(self):
		self.setColumnHidden(0, True)
		self.verticalHeader().setClickable(True)
		self.verticalHeader().sectionPressed.connect(self.addTask)
	def addTask(self, index):
		mainAppWindow.addTask(self.table.record(index).value('process_id'))

class TasksView(RTableView):
	'Table of tasks'
	def __init__(self, db):
		self.table = db.getTable('tasks')
		super(TasksView, self).__init__(self.table)

def main():
	app = QApplication(sys.argv)
	global mainAppWindow
	mainAppWindow = ReportsApp()
if __name__ == '__main__':
	main()