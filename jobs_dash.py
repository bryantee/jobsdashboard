import jobs



fake_street = jobs.Jobs("123 fake st Phoenix, AZ 85255", "2-1-15")
fake_street2 = jobs.Jobs("5496 Yabba-dabba-do st", "2-4-15")

jobDict = {fake_street.job_name: [fake_street.address, fake_street.due]}

for i in jobDict[fake_street.job_name]:
	print(i)

fake_street.add_phase('paint', 'Arturo')
fake_street.add_phase('cleaning', 'Addrienne')
fake_street.add_phase('flooring', 'star flooring')
print(fake_street.phase)


open_jobs = []

def addOpenedJob(job):
	open_jobs.append(job)

addOpenedJob(fake_street.job_name)
addOpenedJob(fake_street2.job_name)

print("jobs that are currently open: \n")

for job in open_jobs:
	print(job)

