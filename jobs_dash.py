import jobs


# Instantiating some jobs
fake_street = jobs.Jobs("123 fake st Phoenix, AZ 85255", "2-1-15")
fake_street2 = jobs.Jobs("5496 Yabba-dabba-do st", "2-4-15")
fake_street3 = jobs.Jobs("9999 yeah yeah yeahs", "2-17-15")


# Adding some phases to the jobs for testing
fake_street.add_phase('paint', 'Arturo')
fake_street.add_phase('cleaning', 'Addrienne')
fake_street.add_phase('flooring', 'star flooring')


# Testing prints to 
for job in jobs.Jobs.open_jobs:
	print(job.address + ' is due ' + job.due)

