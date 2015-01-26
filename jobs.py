
class Jobs():
	def __init__(self, address, city, state, zipcode):
		self.address = address
		self.city = city
		self.state = state
		self.zipcode = zipcode
		self.job_name = ''.join([i for i in address if not i.isdigit()])
		self.job_name = self.job_name[1:]

