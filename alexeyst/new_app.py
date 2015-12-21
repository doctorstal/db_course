import sys

from PyQt4.QtGui import QApplication, QMainWindow, QVBoxLayout, QWidget, QDialog, \
	QMessageBox, QPrinter, QPrintDialog, QTextDocumentWriter, QFileDialog

import business_processes
import companies_contracts
import enter_text_dlg
import main_window_new
import new_task_dlg
import report_generator
import report_window
import select_dlg
import startscreen
import tasks
import users
from database import ProductsDB
from subwidgets import NCompanyView, NProcessView, NTaskView, NUserView


def main():
	app = QApplication(sys.argv)
	global mainAppWindow
	mainAppWindow = NewApp()

	sys.exit(app.exec_())


if __name__ == '__main__':
	main()


class NCompaniesWindow(QMainWindow):
	def __init__(self):
		super(NCompaniesWindow, self).__init__()
		self.companies = {}
		self.initUi()
		self.initWidget()

	def initUi(self):
		self.ui = main_window_new.Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Companies')

	def initWidget(self):
		self.widgetUi = companies_contracts.Ui_Form()
		self.widget = QWidget()
		self.widgetUi.setupUi(self.widget)
		self.setCentralWidget(self.widget)
		self.widgetUi.addCompanyButton.clicked.connect(self.createNewCompany)

		self.initContainerWidget()
		self.updateCompanies()

	def initContainerWidget(self):
		self.containerWidget = QWidget()
		self.containerWidget.setLayout(QVBoxLayout())
		self.widgetUi.companiesContainer.setWidget(self.containerWidget)

	def updateCompanies(self):
		for company in self.companies:
			self.companies[company].hide()

		try:
			self.table.select()
		except:
			self.table = mainAppWindow.db.getTable('contracts_list')

		for rowid in range(self.table.rowCount()):
			record = self.table.record(rowid)
			self.addContract(record)

	def addContract(self, record):
		company = self.getOrCreateCompany(record.value('Company').toString(), record.value('company_id').toInt()[0])

		record.value('contract_id')
		if (not record.value('contract_id').isNull()):
			contract_id = record.value('contract_id').toInt()[0]
			company.addContract(contract_id, record.value('Contract').toString())

		# company.show()

	def getOrCreateCompany(self, name, c_id):
		try:
			return self.companies[name]
		except KeyError:
			self.companies[name] = NCompanyView(c_id, name)
			self.containerWidget.layout().addWidget(self.companies[name])
			self.companies[name].updated.connect(self.updateCompanies)

			return self.companies[name]

	def createNewCompany(self):
		"""Create new company"""
		dlg = QDialog()
		dlgUi = enter_text_dlg.Ui_Dialog()
		dlgUi.setupUi(dlg)
		dlgUi.label.setText('Enter company name:')
		dlg.setWindowTitle('Add new company')

		dlg.exec_()

		if dlgUi.lineEdit.text() != '' and dlg.accepted:
			if mainAppWindow.db.createNewCompany(dlgUi.lineEdit.text()):
				self.updateCompanies()
				QMessageBox.information(self, 'Created', 'Company successfuly created!')
			else:
				QMessageBox.warning(self, 'Failed', 'Failed to create company.')

	pass


class NProcessesWindow(QMainWindow):
	def __init__(self):
		super(NProcessesWindow, self).__init__()
		self.containerWidget = QWidget()
		self.processes = {}
		self.contract_id = -1
		self.contract_name = ''
		self.ui = main_window_new.Ui_MainWindow()
		self.initUi()
		self.initWidget()

	def initUi(self):
		self.ui.setupUi(self)
		self.setWindowTitle('Business Processes')

	def initWidget(self):
		self.widgetUi = business_processes.Ui_Form()
		self.widget = QWidget()
		self.widgetUi.setupUi(self.widget)
		self.setCentralWidget(self.widget)
		self.widgetUi.chooseContractButton.clicked.connect(self.chooseCompany)
		self.widgetUi.addNewProcessButton.clicked.connect(self.createNewProcess)
		self.widgetUi.addNewProcessButton.setDisabled(True)

		self.initContainerWidget()
		# if (not hasattr(mainAppWindow, 'currentContarctId')):
		# 	self.noProcessSelected()

	def initContainerWidget(self):
		self.containerWidget.setLayout(QVBoxLayout())
		self.widgetUi.processesContainer.setWidget(self.containerWidget)
		pass

	def chooseCompany(self):
		mainAppWindow.openWindow('companiesWindow')
		pass

	def hideProcesses(self):
		for p_id in self.processes:
			self.processes[p_id].hide()

	def openProcessData(self, contract_id, contract_name):
		self.contract_id = contract_id
		self.contract_name = contract_name
		self.setWindowTitle('Business processes - [' + contract_name + ']')
		self.widgetUi.addNewProcessButton.setDisabled(False)
		self.hideProcesses()

		self.table = mainAppWindow.db.getProcessesQuery(contract_id)
		self.widgetUi.label.setText(contract_name)

		while self.table.next():
			self.addProcess(self.table.record())

	def updateProcesses(self):
		self.openProcessData(self.contract_id, self.contract_name)

	def addProcess(self, record):
		p_id, p_name = record.value('process_id').toInt()[0], record.value('Process').toString()
		try:
			self.processes[p_id].show()
			self.processes[p_id].updateView(p_id, p_name)
		except KeyError or AttributeError:
			process = NProcessView(p_id, p_name)
			self.processes[p_id] = process
			self.containerWidget.layout().addWidget(process)
		# self.companies[name].updated.connect(self.updateCompanies)

	def noProcessSelected(self):
		self.chooseCompany()

	def createNewProcess(self):
		"""Create new process"""
		dlg = QDialog()
		dlgUi = enter_text_dlg.Ui_Dialog()
		dlgUi.setupUi(dlg)
		dlgUi.label.setText('Enter process name:')
		dlg.setWindowTitle('Add new business process')

		dlg.exec_()

		if dlgUi.lineEdit.text() != '' and dlg.accepted:
			if mainAppWindow.db.createNewProcess(self.contract_id, dlgUi.lineEdit.text()):
				self.updateProcesses()
				QMessageBox.information(self, 'Created', 'Process successfuly created!')
			else:
				QMessageBox.warning(self, 'Failed', 'Failed to create process.')

	pass


class NExecutorsWindow(QMainWindow):
	def __init__(self):
		super(NExecutorsWindow, self).__init__()
		self.initUi()

	# self.initWidget()

	def initUi(self):
		self.users = {}
		self.ui = users.Ui_Executors()
		self.ui.setupUi(self)
		self.setWindowTitle('Executors')
		self.container = QWidget()
		self.container.setLayout(QVBoxLayout())
		self.ui.executorsContainer.setWidget(self.container)
		self.updateUsers()
		self.ui.addNewUserButton.clicked.connect(self.createNewUser)

	def updateUsers(self):
		self.table = mainAppWindow.db.getTable('executor_list')
		for irow in range(self.table.rowCount()):
			self.addUser(self.table.record(irow))

	def addUser(self, record):
		"""

		:param record: QSqlRecord
		:return:
		"""
		u_id = record.value('executor_id').toInt()[0]
		u_name = record.value('executor_name').toString()
		u_tasks_amount = record.value('Tasks').toInt()[0]

		try:
			self.users[u_id].updateView(u_id, u_name, u_tasks_amount)
			self.users[u_id].show()
		except:
			self.users[u_id] = NUserView(u_id, u_name, u_tasks_amount)
			self.container.layout().addWidget(self.users[u_id])


	def createNewUser(self):
		'Create new executor'
		dlg = QDialog()
		dlgUi = enter_text_dlg.Ui_Dialog()
		dlgUi.setupUi(dlg)
		dlg.setWindowTitle('Create new executor')
		dlgUi.label.setText('Enter executors name:')

		dlg.exec_()

		if(dlgUi.lineEdit.text()!='' and dlg.accepted):
			if(mainAppWindow.db.createNewExecutor(dlgUi.lineEdit.text())):
				self.updateUsers()
				QMessageBox.information(self, 'Created', 'User successfuly created!')
			else:
				QMessageBox.warning(self, 'Failed', 'Failed to create user.')


	def initWidget(self):
		self.widgetUi = companies_contracts.Ui_Form()
		self.widget = QWidget()
		self.widgetUi.setupUi(self.widget)

	pass


class NTasksWindow(QMainWindow):
	def __init__(self):
		self.process_id = -1
		super(NTasksWindow, self).__init__()
		self.tasks = {}
		self.ui = main_window_new.Ui_MainWindow()
		self.initUi()
		self.initWidget()

	def initUi(self):
		self.ui.setupUi(self)
		self.setWindowTitle('Tasks')

	def initWidget(self):

		self.widget = QWidget()
		self.widgetUi = tasks.Ui_Form()
		self.widgetUi.setupUi(self.widget)

		self.setCentralWidget(self.widget)
		self.containerWidget = QWidget()
		self.containerWidget.setLayout(QVBoxLayout())
		self.widgetUi.tasksContainer.setWidget(self.containerWidget)
		self.widgetUi.chooseProcessButton.clicked.connect(self.chooseProcess)
		self.widgetUi.addNewTaskButton.clicked.connect(self.createNewTask)
		self.widgetUi.addNewTaskButton.setEnabled(False)

	def chooseProcess(self):
		mainAppWindow.openWindow('processesWindow')

	def updateView(self):
		self.openTasksData(self.process_id, self.process_name)

	def openTasksData(self, p_id, p_name):
		self.process_id = p_id
		self.process_name = p_name

		self.widgetUi.addNewTaskButton.setEnabled(True)
		self.widgetUi.label.setText(p_name)
		self.setWindowTitle('Tasks - [' + p_name + ']')

		self.hideTasks()
		self.table = mainAppWindow.db.getTasksQuery(p_id)

		while self.table.next():
			self.addTask(self.table.record())


	def hideTasks(self):
		"""hide all tasks"""
		for t_id in self.tasks:
			self.tasks[t_id].hide()

	def addTask(self, record):

		t_id = record.value('task_id').toInt()[0]
		t_name = record.value('Task name').toString()
		t_status = record.value('Status').toString()+' ('+record.value('executor_name').toString()+')'
		t_status_id = record.value('status_id').toInt()[0]
		t_has_next = t_status_id < 2 and (t_status_id > 0 or record.value('prev_id').toInt()[0] == 0)

		try:
			self.tasks[t_id].show()
			self.tasks[t_id].updateView(t_id, t_name, t_status, t_has_next)
		except KeyError or AttributeError:
			task = NTaskView(t_id, t_name, t_status, t_has_next)
			self.tasks[t_id] = task
			self.containerWidget.layout().addWidget(task)
			task.proceeded.connect(self.procceedTaskStatus)
			task.changeClicked.connect(self.changeTaskExecutor)

	def procceedTaskStatus(self, t_id):
		mainAppWindow.db.proceedTaskStatus(t_id)
		self.updateView()
	pass

	def changeTaskExecutor(self, t_id):
		dlg = QDialog()
		selectDlgUi = select_dlg.Ui_Dialog()
		selectDlgUi.setupUi(dlg)
		table = mainAppWindow.db.getTable('executors')
		user_ids = []
		for rowid in range(table.rowCount()):
			record = table.record(rowid)
			selectDlgUi.comboBox.addItem(record.value('executor_name').toString())
			user_ids.append(record.value('executor_id').toInt()[0])

		selectDlgUi.label.setText('Select employee:')

		dlg.exec_()
		user_id = user_ids[selectDlgUi.comboBox.currentIndex()]
		if mainAppWindow.db.changeExecutor(t_id, user_id):
			QMessageBox.information(self, 'Success', 'Responsible person successfully changed!')
			self.updateView()
		else:
			QMessageBox.warning(self, 'Failed', 'Failed to change responsible')


	def createNewTask(self):
		"""Create new task"""
		dlg = QDialog()
		dlgUi = new_task_dlg.Ui_Dialog()
		dlgUi.setupUi(dlg)
		table = mainAppWindow.db.getTable('executors')
		user_ids = []
		for rowid in range(table.rowCount()):
			record = table.record(rowid)
			dlgUi.comboBox.addItem(record.value('executor_name').toString())
			user_ids.append(record.value('executor_id').toInt()[0])

		dlg.exec_()
		user_id = user_ids[dlgUi.comboBox.currentIndex()]

		if(dlgUi.lineEdit.text()!='' and dlg.accepted):
			if(mainAppWindow.db.createNewTask(self.process_id,
									 dlgUi.lineEdit.text(),
									user_id)):
				QMessageBox.information(self, 'Created', 'Task successfuly created!')
			else:
				QMessageBox.warning(self, 'Failed', 'Failed to create task.')

		self.updateView()


class NReportWindow(QMainWindow):
	def __init__(self):
		super(NReportWindow, self).__init__()
		self.ui = report_window.Ui_MainWindow()
		self.initUi()

	def initUi(self):
		self.ui.setupUi(self)
		self.setWindowTitle('Report')
		self.ui.textEdit.setHtml(report_generator.Generator(mainAppWindow.db).generateFullReport())
		self.ui.printButton.clicked.connect(self.printDocument)
		self.ui.saveButton.clicked.connect(self.saveDocument)

	def printDocument(self):
		printer = QPrinter()
		dialog = QPrintDialog(printer)
		# printer.setOutputFileName("print.ps")
		dialog.exec_()
		if dialog.accepted():
			self.ui.textEdit.print_(printer)

		# self.ui.textEdit.print_(QPrinter())

	def saveDocument(self):
		print(self.ui.textEdit.toHtml())
		writer = QTextDocumentWriter()
		fileName = QFileDialog.getOpenFileName(self, "Save report", "", "Html Files (*.html )");
		writer.setFileName(fileName)
		writer.setFormat('html')

		writer.write(self.ui.textEdit.document())

	pass


class NStartScreen(QWidget):
	'StartScreen for reports app'

	def __init__(self):
		super(NStartScreen, self).__init__()
		self.initUi()
		self.initButtons()

	def initUi(self):
		self.ui = startscreen.Ui_Form()
		self.ui.setupUi(self)

	def initButtons(self):
		self.ui.companiesButton.clicked.connect(self.openCompaniesWindow)
		self.ui.processesButton.clicked.connect(self.openProcessesWindow)
		self.ui.responsiblesButton.clicked.connect(self.openExecutorsWindow)
		self.ui.tasksButton.clicked.connect(self.openTasksWindow)
		self.ui.reportButton.clicked.connect(self.openReportWindow)

	def openCompaniesWindow(self):
		mainAppWindow.openWindow('companiesWindow')

	def openProcessesWindow(self):
		mainAppWindow.openWindow('processesWindow')

	def openExecutorsWindow(self):
		mainAppWindow.openWindow('executorsWindow')

	def openTasksWindow(self):
		mainAppWindow.openWindow('tasksWindow')

	def openReportWindow(self):
		mainAppWindow.openWindow('reportWindow')

	pass


class NewApp(QMainWindow):
	def __init__(self):
		'Constrructor'

		super(NewApp, self).__init__()
		self.db = ProductsDB()
		self.db.connect("localhost:1521", "sql_developer", "Can_I_have_a_cookie");

		self.windows = {}
		self.initWindowClasses()
		self.ui = main_window_new.Ui_MainWindow()
		self.initUi()
		self.show()

	def openWindow(self, name):

		try:
			self.getWindow(name).raise_()
			self.getWindow(name).activateWindow()
		except KeyError:
			cls = self.windowClasses[name]
			self.setWindow(name, cls())
			self.getWindow(name).move(mainAppWindow.x() + 10, mainAppWindow.y() + 10)

		self.getWindow(name).show()

	def initWindowClasses(self):
		self.windowClasses = {}
		self.windowClasses['companiesWindow'] = NCompaniesWindow
		self.windowClasses['processesWindow'] = NProcessesWindow
		self.windowClasses['executorsWindow'] = NExecutorsWindow
		self.windowClasses['tasksWindow'] = NTasksWindow
		self.windowClasses['reportWindow'] = NReportWindow

	def initUi(self):
		self.ui.setupUi(self)
		self.startScreen = NStartScreen()
		self.setCentralWidget(self.startScreen)

	def getWindow(self, name):
		return self.windows[name]

	def setWindow(self, name, window):
		self.windows[name] = window;

	pass
