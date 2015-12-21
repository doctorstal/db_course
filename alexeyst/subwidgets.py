from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import QWidget, QGroupBox, QLabel, QVBoxLayout, QFrame, QSizePolicy, QMainWindow, QMessageBox, QDialog

import edit_contract_text
import enter_text_dlg
import new_app
import one_company_view
import one_contract_view
import one_process_view
import one_task_view
import one_user


class NContractView(QFrame):
	def __init__(self, c_id, name):
		super(NContractView, self).__init__()
		self.id = int(c_id)
		self.updateView(name)

	def updateView(self, name):
		'update view'
		self.name = name
		self.initUi()

	def initUi(self):
		if (not hasattr(self, 'ui')):
			self.ui = one_contract_view.Ui_Frame()
			self.ui.setupUi(self)
		self.ui.label.setText(self.name)
		self.ui.showTextButton.clicked.connect(self.openTextEditor)
		self.ui.showTasksButton.clicked.connect(self.openProcesses)

	def openTextEditor(self):
		if (not hasattr(self, 'editor')):
			self.editor = QMainWindow()

			self.editorUi = edit_contract_text.Ui_editWindow()
			self.editorUi.setupUi(self.editor)
			self.editor.setWindowTitle(self.editor.windowTitle() + ' - [' + self.name + ']')
			self.editorUi.saveButton.clicked.connect(self.saveContractText)

		self.editor.show()
		self.editor.activateWindow()

		self.editorUi.plainTextEdit.setPlainText(self.getContractText())

	def getContractText(self):
		return self.getDB().getContractText(self.id)
		pass

	def saveContractText(self):
		save_ok = self.getDB().saveContractText(self.id, self.editorUi.plainTextEdit.toPlainText())
		if (save_ok):
			QMessageBox.information(self.editor, 'Success', 'Text was sent to DB!')
		else:
			QMessageBox.warning(self.editor, 'Failure', 'Failed to send text to DB')

	def openProcesses(self):
		new_app.mainAppWindow.currentContractId = self.id

		new_app.mainAppWindow.openWindow('processesWindow')
		new_app.mainAppWindow.getWindow('processesWindow').openProcessData(self.id, self.name)

	def getDB(self):
		return new_app.mainAppWindow.db

	pass


class NCompanyView(QGroupBox):
	updated = pyqtSignal()

	def __init__(self, c_id, name):
		super(NCompanyView, self).__init__()
		self.id = c_id
		self.name = name
		self.contracts = {}
		self.initUi()

	def initUi(self):
		self.ui = one_company_view.Ui_GroupBox()
		self.ui.setupUi(self)
		self.setTitle(self.name)
		self.empty = QLabel()
		self.empty.setText('No contracts yet')
		self.ui.contractsContainer.setLayout(QVBoxLayout())

		self.ui.contractsContainer.layout().addWidget(self.empty)

		self.ui.collapseButton.clicked.connect(self.collapseContracts)
		# self.collapseContracts()
		self.ui.addContractButton.clicked.connect(self.createContract)

	def collapseContracts(self):
		if (self.ui.contractsContainer.isHidden()):
			self.ui.contractsContainer.show()
			self.ui.collapseButton.setArrowType(Qt.UpArrow)
		else:
			self.ui.contractsContainer.hide()
			self.ui.collapseButton.setArrowType(Qt.DownArrow)

	def addContract(self, c_id, name):
		try:
			self.contracts[c_id].updateView(name)
		except:
			self.contracts[c_id] = NContractView(c_id, name)
			# self.ui.page.layout().addWidget(self.contracts[id])
			self.ui.contractsContainer.layout().addWidget(self.contracts[c_id])

		self.empty.hide()
		# self.ui.contractsContainer.show()
		self.setTitle(self.name + ' (' + str(len(self.contracts)) + ' contracts)')

	def createContract(self):
		'Create new company'
		dlg = QDialog()
		dlgUi = enter_text_dlg.Ui_Dialog()
		dlgUi.setupUi(dlg)
		dlgUi.label.setText('Enter contract name:')
		dlg.setWindowTitle('Add new contract - [' + self.name + ']')

		dlg.exec_()

		if (dlgUi.lineEdit.text() != '' and dlg.accepted):
			if (new_app.mainAppWindow.db.createNewContract(self.id, dlgUi.lineEdit.text())):
				self.updated.emit()
				QMessageBox.information(self, 'Created', 'Company successfuly created!')
			else:
				QMessageBox.warning(self, 'Failed', 'Failed to create company.')

	pass


class NProcessView(QFrame):
	def __init__(self, p_id, name):
		super(NProcessView, self).__init__()
		self.p_id = p_id
		self.name = name
		self.initUi()
		self.updateView(p_id, name)

	def initUi(self):
		self.ui = one_process_view.Ui_Frame()
		self.ui.setupUi(self)
		self.ui.showTasksButton.clicked.connect(self.openTasks)

	def openTasks(self):
		new_app.mainAppWindow.currentProcessId = self.p_id

		new_app.mainAppWindow.openWindow('tasksWindow')
		new_app.mainAppWindow.getWindow('tasksWindow').openTasksData(self.p_id, self.name)

	def updateView(self, p_id, name):
		self.ui.label.setText(self.name)


class NTaskView(QFrame):
	proceeded = pyqtSignal(int)
	changeClicked = pyqtSignal(int)

	def __init__(self, t_id, t_name, t_status, t_has_next):
		super(NTaskView, self).__init__()
		self.t_id = t_id
		self.name = t_name
		self.initUi()
		self.updateView(t_id, t_name, t_status, t_has_next)

	def initUi(self):
		self.ui = one_task_view.Ui_Frame()
		self.ui.setupUi(self)
		self.ui.proceedStatusButton.clicked.connect(self.proceedStatus)
		self.ui.changeExecutorButton.clicked.connect(self.changeExecutor)

	def updateView(self, t_id, t_name, t_status, t_has_next):
		self.name = t_name
		self.ui.label.setText(self.name)
		self.ui.status.setText(t_status)
		self.ui.proceedStatusButton.setEnabled(t_has_next)

	def hasNextStatus(self):
		self.ui.proceedStatusButton.setEnabled(True)

	def proceedStatus(self):
		self.proceeded.emit(self.t_id)

	def changeExecutor(self):
		self.changeClicked.emit(self.t_id)


class NUserView(QWidget):
	def __init__(self, u_id, u_name, u_tasks_amount):
		super(NUserView, self).__init__()
		self.u_id = u_id
		self.name = u_name
		self.tasks_amount = u_tasks_amount
		self.initUi()
		self.updateView(u_id, u_name, u_tasks_amount)

	def updateView(self, u_id, u_name, u_tasks_amount):
		self.tasks = {}
		self.u_id = u_id
		self.name = u_name
		self.tasks_amount = u_tasks_amount

		self.ui.userNameButton.setText(self.name + ' (' + str(u_tasks_amount) + ' tasks)')

	def initUi(self):
		self.ui = one_user.Ui_executorForm()
		self.ui.setupUi(self)
		self.ui.userNameButton.clicked.connect(self.expandUserStatistics)
		self.ui.tasksBox.setHidden(True)
		self.ui.tasksBox.setLayout(QVBoxLayout())

	def expandUserStatistics(self):
		self.ui.tasksBox.setHidden(not self.ui.tasksBox.isHidden())
		if not self.ui.tasksBox.isHidden():
			self.updateTasks()

	def addTask(self, record):
		"""
		QSqlQuery
		:param record:
		:return:
		"""
		t_id = record.value('task_id').toInt()[0]
		t_name = record.value('Task name').toString()
		t_status = record.value('Status').toString() + ' (' + record.value('executor_name').toString() + ')'
		t_status_id = record.value('status_id').toInt()[0]
		t_has_next = t_status_id < 2 and (t_status_id > 0 or record.value('prev_id').toInt()[0] == 0)

		try:
			self.tasks[t_id].show()
			self.tasks[t_id].updateView(t_id, t_name, t_status, t_has_next)
		except KeyError or AttributeError:
			task = NTaskView(t_id, t_name, t_status, t_has_next)
			self.tasks[t_id] = task
			self.ui.tasksBox.layout().addWidget(task)
			task.proceeded.connect(self.procceedTaskStatus)
			task.changeClicked.connect(self.changeTaskExecutor)

	def updateTasks(self):
		query = new_app.mainAppWindow.db.getExecutorTasksQuery(self.u_id)
		while (query.next()):
			self.addTask(query.record())

	def procceedTaskStatus(self, t_id):
		pass

	def changeTaskExecutor(self, t_id):
		pass

	pass
