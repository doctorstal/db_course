
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
		:param db: database.ProductsDB
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
		res = '<h2>Here is list of tasks, finished last week:</h2>'
		return res

	def fetchTaskCompleters(self):
		"""
		List of executors, that've done tasks. With count of accomplished tasks
		:return: string list of executors
		"""
		res = """<h2>Here you can see, who've done that tasks (don't forget to thank them all):</h2>"""
		return res

	def fetchAttentionContractData(self):
		"""
		Contracts that requires attention
		:return:
		"""
		res = """<br/>Ok, now when everybody got their thanks and we know how cool we are, lets talk about business."""
		res += """<br/><h2>Here is list of contracts, that requires your attention:</h2>"""
		res += '\n' + self.fetchUnplannedContractsData()
		res += '\n' + self.fetchUnfinishedContractsData()
		return res

	def fetchUnfinishedContractsData(self):
		"""
		List of unfinished contracts and processes/tasks that is not finished yet
		:return: string
		"""
		res = """<h3> Contracts that have unfinished tasks:</h3>"""
		return res

	def fetchUnplannedContractsData(self):
		"""
		List of contracts, that is not planned yet
		:return: string
		"""
		res = """\n<h3> Contracts that is not planned yet:</h3>"""
		return res


	def fetchViolatorsList(self):
		"""
		The Blackest of All Black Lists.
		:return: string
		"""
		res = """<br/>But before you go: remember to do things in time. Not like those deadline violators from last week.<br/>"""
		res += """<br/><h4>You remember that you have only 1 day for each task, right?</h4>"""
		res += """<br/>We will not publish their names, but we know..."""
		res += """<br/><br/>You don't belive me? Ok, see that black list and check:"""
		return res


