import time

from database import ProductsDB


class Generator(object):
	"""
	Should generate report for one week.
	Report should contain folowing data:
		- List of tasks, finished last week
		- Who've done that tasks?
		- Unfinished contracts data:
			- list of tasks
		- Unplanned contracts
		- Deadline violators
	"""

	def __init__(self, db):
		"""
		Constructor
		:param db: ProductsDB
		:return:
		"""
		super(Generator, self).__init__()
		self.db = db

	def generateFullReport(self):
		"""

		:return: string containing all report data
		"""
		res = '<body><h1>Weekly report</h1>'
		res += self.fetchFinishedTasks()
		res += self.fetchTaskCompleters()
		res += self.fetchAttentionContractData()
		res += """<br/> <h2>Ok, so lets get to work.</h2><br/><br/><br/>"""
		res += self.fetchViolatorsList()
		res += """<br/><br/><br/>See ya next week!"""
		res += """</body>"""
		return res

	def fetchFinishedTasks(self):
		"""
		List of finished tasks with time intervals it took to accomplish them
		:return: string list of tasks
		"""

		done_table = self.db.getTable('report_done_tasks')
		if done_table.rowCount() <= 0:
			return ''
		res = '<h2>Here is list of tasks, finished last week:</h2><br/>'
		res += '<table><tr><th width="60%">Task name</th><th width="40%">Process</th></tr>'

		for irow in range(done_table.rowCount()):
			res += '<tr><td>' + done_table.record(irow).value('task_name').toString() + '</td><td>' + done_table.record(
					irow).value('process_name').toString() + '</td></tr>'

		res += '</table>'
		return res

	def fetchTaskCompleters(self):
		"""
		List of executors, that've done tasks. With count of accomplished tasks
		:return: string list of executors
		"""
		done_table = self.db.getTable('report_done_tasks')
		if done_table.rowCount() <= 0:
			return ''
		res = """<h2>Here you can see, who've done that tasks (don't forget to thank them all):</h2>"""
		res += '<table><tr><th width="60%">Executor name</th><th width="10%">Tasks done</th></tr>'

		completers = {}
		for irow in range(done_table.rowCount()):
			eName = done_table.record(irow).value('executor_name').toString()
			try:
				completers[eName] += 1
			except KeyError:
				completers[eName] = 1

		for name in completers:
			res += '<tr><td>' + name + '</td><td>' + str(completers[name]) + '</td></tr>'

		res += '</table>'
		return res

	def fetchAttentionContractData(self):
		"""
		Contracts that requires attention
		:return:
		"""
		res = """<br/>Ok, now when everybody got their thanks and we know how cool we are, lets talk about business."""
		res += """<br/><h2>Here is list of contracts, that requires your attention:</h2>"""
		unplaned = '\n' + self.fetchUnplannedContractsData()
		unfinished = '\n' + self.fetchUnfinishedContractsData()

		return res + unplaned + unfinished if len(unfinished) > 0 or len(unplaned) > 0 else ''

	def fetchUnfinishedContractsData(self):
		"""
		List of unfinished contracts and processes/tasks that is not finished yet
		:return: string
		"""
		done_table = self.db.getTable('report_unfinished_contracts')
		if done_table.rowCount() <= 0:
			return ''
		res = """<h3> Contracts that have unfinished tasks:</h3>"""
		res += '<table><tr><th width="25%">Contract</th><th width="25%">Process</th><th width="25%">Task</th><th width="25%">Responsible</th></tr>'
		for irow in range(done_table.rowCount()):
			res += '<tr>'
			res += '<td>' + done_table.record(irow).value('contract_name').toString() + '</td>'
			res += '<td>' + done_table.record(irow).value('process_name').toString() + '</td>'
			res += '<td>' + done_table.record(irow).value('task_name').toString() + '</td>'
			res += '<td>' + done_table.record(irow).value('executor_name').toString() + '</td>'
			res += '</tr>'
		res += '</table>'

		return res

	def fetchUnplannedContractsData(self):
		"""
		List of contracts, that is not planned yet
		:return: string
		"""
		done_table = self.db.getTable('report_unplanned_contracts')
		if done_table.rowCount() <= 0:
			return ''
		res = """\n<h3> Contracts that is not planned yet:</h3>"""
		res += '<table><tr><th width="60%">Contract name</th></tr>'
		for irow in range(done_table.rowCount()):
			res += '<tr><td>' + done_table.record(irow).value('contract_name').toString() + '</td></tr>'
		res += '</table>'

		return res

	def fetchViolatorsList(self):
		"""
		The Blackest of All Black Lists.
		:return: string
		"""
		done_table = self.db.getTable('report_deadline_violators')
		if done_table.rowCount() <= 0:
			return ''
		res = """<br/>But before you go: remember to do things in time. Not like those deadline violators from last week.<br/>"""
		res += """<br/><h4>You remember that you have only 1 day for each task, right?</h4>"""
		res += """<br/>We will not publish their names, but we know..."""
		res += """<br/><br/>You don't belive me? Ok, see that black list and check:"""

		res += '<table><tr><th width="40%">(not such) Responsible</th><th width="40%">Task name</th><th width="20%">Time taken (HH:MM:SS)</th></tr>'
		for irow in range(done_table.rowCount()):
			res += '<tr>'
			res += '<td>' + done_table.record(irow).value('executor_name').toString() + '</td>'
			res += '<td>' + done_table.record(irow).value('task_name').toString() + '</td>'
			res += '<td>' + self.formatTime(
					done_table.record(irow).value('completion_time').toFloat()[0]) + '</td>'
			res += '</tr>'
		res += '</table>'

		return res

	def formatTime(self, days):
		"""

		:param days: float
		:return: str
		"""

		format = '%H:%M:%S'

		return time.strftime(format, time.gmtime(int(days * 24 * 60 * 60))) if (days<1) else str(int(days)) + ' day(s)'
