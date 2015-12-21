# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 01:46:46 2015

@author: alexeyst
"""
from PyQt4.QtSql import *
from PyQt4.QtCore import QObject


class ProductsDB(QObject):
	'This class wraps all requests to database'

	def __init__(self):
		self.db = QSqlDatabase.addDatabase("QODBC");
		self.tables = {}

		pass

	def __del__(self):
		#        self.db = QSqlDatabase();
		for table_name in self.tables:
			self.tables[table_name].clear()
		self.db.close()

	def connect(self, host, username, password):

		self.db.setHostName(host)
		#         self.db.setDatabaseName(username + '/' + password + '@' + host +'/xe')
		self.db.setDatabaseName('DSN=odbc-xe;DRIVER={Oracle ODBC Driver};DBQ=XE;')
		self.db.setUserName(username)
		self.db.setPassword(password)
		ok = self.db.open();
		if ok:
			print('Connected: ', ok)
		else:
			print('Not connected: ', self.db.lastError().text())

		return ok

	def getContractText(self, c_id):
		query = QSqlQuery(self.db)
		query.prepare("""SELECT text FROM contracts WHERE contract_id=:p_id;""")
		query.bindValue(':p_id', c_id)
		query.exec_()
		if (query.next()):
			res = query.value(0).toString()
			query.clear()
			return res
		else:
			return ''
	def saveContractText(self, c_id, text):
		query = QSqlQuery(self.db)
		query.prepare("""CALL update_contract_text(:p_id, :p_text);""")
		query.bindValue(':p_id', c_id)
		query.bindValue(':p_text', text)
		query.exec_()
		if (query.lastError().isValid()):
			print('save text fail: ', query.lastError().text(), self.db.lastError().text())
			return False
		else:
			return True

	def getProcessesQuery(self, c_id):
		query = QSqlQuery(self.db)
		query.prepare("""SELECT * FROM processes_list WHERE contract_id=:p_id;""")
		query.bindValue(':p_id', c_id)
		query.exec_()
		if (query.lastError().isValid()):
			print('add select process fail: ', query.lastError().text(), self.db.lastError().text())
		else:
			print('Success query')
		return query

	def getTasksQuery(self, p_id):
		query = QSqlQuery()
		query.prepare("""SELECT * FROM tasks_list WHERE process_id=:p_id ORDER BY task_id;""")
		query.bindValue(':p_id', p_id)
		query.exec_()
		if (query.lastError().isValid()):
			print('select task fail: ', query.lastError().text(), self.db.lastError().text())
		else:
			print('Success query')
		return query

	def proceedTaskStatus(self, t_id):
		query = QSqlQuery(self.db)
		query.prepare("""CALL proceed_task_status(:t_id);""")
		query.bindValue(':t_id', t_id)
		query.exec_()
		if (query.lastError().isValid()):
			print('proceed task fail: ', query.lastError().text(), self.db.lastError().text())
			return False
		else:
			print('Success query')
			return True

	def changeExecutor(self, t_id, e_id):
		query = QSqlQuery(self.db)
		query.prepare("""CALL change_executor(:e_id, :t_id);""")
		query.bindValue(':t_id', t_id)
		query.bindValue(':e_id', e_id)
		query.exec_()
		if (query.lastError().isValid()):
			print('change executor fail: ', query.lastError().text(), self.db.lastError().text())
			return False
		else:
			return True

	def getExecutorTasksQuery(self, e_id):
		query = QSqlQuery(self.db)
		query.prepare("""SELECT * FROM tasks_list WHERE executor_id=:e_id;""")
		query.bindValue(':e_id', e_id)
		query.exec_()
		if (query.lastError().isValid()):
			print('select tasks fail: ', query.lastError().text(), self.db.lastError().text())
		else:
			print('Success query')
		return query


	# CREATING NEW
	def createNewExecutor(self, name):
		query = QSqlQuery(self.db)
		query.prepare("""CALL add_executor(:p_name);""")
		query.bindValue(':p_name', str(name))
		query.exec_()
		if (query.lastError().isValid()):
			print('add executor fail: ', query.lastError().text(), self.db.lastError().text())
			return False
		else:
			return True

	def createNewCompany(self, name):
		query = QSqlQuery(self.db)
		query.prepare("""CALL add_company(:p_name);""")
		query.bindValue(':p_name', str(name))
		query.exec_()
		if (query.lastError().isValid()):
			print('fail: ', query.lastError().text(), self.db.lastError().text())
			return False
		else:
			return True

	def createNewContract(self, company_id, contract_name):
		query = QSqlQuery(self.db)
		query.prepare("""CALL add_contract(:company_id, :p_name);""")
		query.bindValue(':company_id', str(company_id))
		query.bindValue(':p_name', str(contract_name))
		query.exec_()
		if (query.lastError().isValid()):
			print('fail: ', query.lastError().text(), self.db.lastError().text())
			return False
		else:
			return True

	def createNewProcess(self, contract_id, process_name):
		query = QSqlQuery(self.db)
		query.prepare("""CALL add_process(:p_contract_id, :p_name);""")
		query.bindValue(':p_contract_id', int(contract_id))
		query.bindValue(':p_name', str(process_name))
		query.exec_()
		if (query.lastError().isValid()):
			print('fail: ', query.lastError().text(), self.db.lastError().text())
			return False
		else:
			return True

	def createNewTask(self, process_id, task_name, executor_id):
		query = QSqlQuery(self.db)
		query.prepare("""CALL add_task(:p_pid, :p_tname, :p_eid);""")

		query.bindValue(':p_pid', int(process_id));
		query.bindValue(':p_tname', str(task_name));
		query.bindValue(':p_eid', int(executor_id));
		query.exec_()
		if (query.lastError().isValid()):
			print('fail: ', query.lastError().text(), self.db.lastError().text())
			return False
		else:
			return True

	def getTable(self, table_name):
		"""

		:param table_name: string
		:return: QSqlTableModel
		"""
		table = QSqlTableModel(None, self.db)
		table.setTable(table_name)
		table.select()

		self.tables[table_name] = table
		return table


import sys
from PyQt4.QtGui import QApplication

if __name__ == '__main__':
	app = QApplication(sys.argv)
	db = ProductsDB()
	db.connect("localhost:1521", "sql_developer", "Can_I_have_a_cookie")
	db.changeExecutor(8, 15)

	sys.exit()
