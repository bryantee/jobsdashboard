

class Jobs():
    
    open_jobs = []
    closed_jobs = []

    def __init__(self, address, due, price=0):
        self.address = address
        Jobs.open_jobs.append(self)
        self.due = due   # Due date
        self.price = float(price)
        self.phase = {}
    def __str__(self):
        return self.address

    def add_phase(self, trade, vendor):
        self.phase[trade] = vendor

    def close_job(self):
        Jobs.open_jobs.remove(self)
        Jobs.closed_jobs.append(self)

    @classmethod
    def current_jobs(cls):
        print(open_jobs)

