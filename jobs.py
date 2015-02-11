
class Jobs():
	
	open_jobs = []

	def __init__(self, address, due):
		self.address = address
		Jobs.open_jobs.append(self)
		# Commenting out some features that I don't want to implement now
		#self.city = city
		#self.state = state
		#self.zipcode = zipcode
		#self.job_name = ''.join([i for i in address if not i.isdigit()])
		#self.job_name = self.job_name[1:]
		self.due = due
		self.phase = {}

	def add_phase(self, trade, vendor):
		self.phase[trade] = vendor

	@classmethod
	def current_jobs(cls):
		print(open_jobs)

