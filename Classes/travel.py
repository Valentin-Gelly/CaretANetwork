class Travel:

    def __init__(self, hour, travel):
        self.hour = hour
        self.travel = travel

    def __str__(self):
        return ''+self.hour + ' '+ self.travel

    def getHour(self):
        return self.hour

    def getTravel(self):
        return self.travel