class Road():
    def __init__(self, start, stop, distance):
        self.start=start
        self.stop = stop
        self.distance = distance

    def getDistanceByRoad(self):
        return self.distance

    def getRoad(self):
        return self.start, self.stop

    def getRoadByStartAndStop(self, start, stop):
        if self.start == start and self.stop == stop:
            return self.distance
        else:
            return "Error"


