
class Jobs():
	
	open_jobs = []

	def __init__(self, address, due):
		self.address = address
		Jobs.open_jobs.append(self)
		self.due = due
		self.phase = {}
	def __str__(self):
		return self.address

	def add_phase(self, trade, vendor):
		self.phase[trade] = vendor

	@classmethod
	def current_jobs(cls):
		print(open_jobs)

