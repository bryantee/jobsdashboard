import jobs

fake_street = jobs.Jobs("123 fake st", "Phoenix", "AZ", "85257")

print(fake_street.job_name, ": ", fake_street.address) 

jobDict = {fake_street.job_name: [fake_street.address, fake_street.city, fake_street.state, fake_street.zipcode]}

for i in jobDict[fake_street.job_name]:
	print(i)

fake_street.add_phase('paint', 'Arturo')
print(fake_street.phase)