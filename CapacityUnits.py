
#A module to hold the classes / types of basic Capacity building blocks(units) Probably will refactor later as this may be uneeded

class Requests:
    def __init__(self, Count):
        self.TotalThreads = Count
        self.ActiveThreads = Count
        self.IdleThreads = 0

    def getTotalThreadCount(self):
        return self.TotalThreads

    def getActiveThreadCount(self):
        return self.ActiveThreads

    def getIdleThreadCount(self):
        return self.IdleThreads

    def LittlesLaw(self, throughput, responseTime):
        self.ActiveThreads = throughput * responseTime
        self.IdleThreads = self.TotalThreads - self.ActiveThreads

class Throughput:
    def __init__(self, Rate):
        self.Rate = Rate

class ResponseTime:
    def __init__(self, Time):
        self.Time = Time