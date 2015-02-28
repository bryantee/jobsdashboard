import jobs


# Instantiating some jobs
fake_street = jobs.Jobs("123 Fake St Phoenix, AZ", "2-1-15")
fake_street2 = jobs.Jobs("5496 E 1st St Tucson, AZ", "2-4-15")
fake_street3 = jobs.Jobs("9999 S Lake Dr, Phoenix, AZ", "2-17-15")
fake_street4 = jobs.Jobs("1983 'Mermaid I should be' St", "3-16-15")



# Adding some phases to the jobs for testing
# Job 1
fake_street.add_phase('Paint', 'Arturo')
fake_street.add_phase('Cleaning', 'Addrienne')
fake_street.add_phase('Flooring', 'Star flooring')
# Job 2
fake_street2.add_phase('Paint', 'Ramsey Painting')
fake_street2.add_phase('Cleaning', 'La Maids')
fake_street2.add_phase('Repairs', 'Arts Handyworks')
# Job 3
fake_street3.add_phase('Repairs', 'Magna Building')
fake_street3.add_phase('Landscape', 'Jason')
fake_street3.add_phase('Electrical', 'Ruoff Electric')
fake_street3.add_phase('Supervisor', 'Kevin')
# Job 4
fake_street4.add_phase('HVAC', 'Custom Air')
fake_street4.add_phase('Repairs', 'Arts Hand Works')
fake_street4.add_phase('Shower Enclosure', 'Diamond Glass')
fake_street4.add_phase('Shower / Backsplash Tile', 'Master Stonework')


# Testing method for printing jobs, due date and phases
def showOpenJobs():
	print('\n')
	print('The number of currently open jobs is: ', openJobCount(), '\n')

	for job in jobs.Jobs.open_jobs:
		print(job.address + ' is due on ' + job.due)
		for i in job.phase:
			print(' - ', i, ': ', job.phase[i])
		print('\n')

# test out showing number of open jobs
def openJobCount():
	return len(jobs.Jobs.open_jobs)

# Test show closed jobs count
def closedJobCount():
	return len(jobs.Jobs.closed_jobs)
















