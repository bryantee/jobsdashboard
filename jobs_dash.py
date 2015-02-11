import jobs


# Instantiating some jobs
fake_street = jobs.Jobs("123 fake st Phoenix, AZ 85255", "2-1-15")
fake_street2 = jobs.Jobs("5496 Yabba-dabba-do st", "2-4-15")
fake_street3 = jobs.Jobs("9999 yeah yeah yeahs", "2-17-15")
fake_street4 = jobs.Jobs("blah blah blah", "2-22-15")


# Adding some phases to the jobs for testing
# Job 1
fake_street.add_phase('paint', 'Arturo')
fake_street.add_phase('cleaning', 'Addrienne')
fake_street.add_phase('flooring', 'star flooring')
# Job 2
fake_street2.add_phase('paint', 'Ramsey Painting')
fake_street2.add_phase('Cleaning', 'La Maids')
# Job 3
fake_street3.add_phase('Repairs', 'Magna Building')


# Testing method for printing jobs, due date and phases
def showOpenJobs():
	for job in jobs.Jobs.open_jobs:
		print(job.address + ' is due ' + job.due)
		for i in job.phase:
			print(' - ', i, ': ', job.phase[i], '\n')

# test out showing number of open jobs
def openJobCount():
	return len(jobs.Jobs.open_jobs)

print('Number of open jobs: ', openJobCount())








