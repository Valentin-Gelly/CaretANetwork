class Bus:
    def __init__(self, nbPlace, timeReload, speed, travel):
        self.nbPlace: int = nbPlace
        self.nbPersonnes: int = 0
        self.timeReload: int = timeReload
        self.speedMetter: int = speed[0]
        self.speedTime: int = speed[1]
        self.travel = []
        for stop in travel:
            self.travel.append(stop)
        self.position = self.travel[0]
        self.distanceFromNextStop = 0
        self.listePeople = []

    def __str__(self):
        return 'bus de ' + str(
            self.nbPersonnes) + ' personnes, qui réalise le trajet ' + self.travel + ' à une vitesse de ' + str(
            self.speed) + ', il met ' + str(
            self.timeReload) + ' pour récupérer une personne'

    def getAllStop(self):
        return self.travel

    def getNbPersonnes(self):
        return self.nbPersonnes

    def getTimeReload(self):
        return self.timeReload

    def getSpeedMetter(self):
        return self.speedMetter

    def getSpeedTime(self):
        return self.speedTime

    def getTravel(self):
        return self.travel

    def remplirUnePersonne(self, personne):
        if self.nbPersonnes != self.nbPersonnes:
            self.nbPersonnes += 1
            self.listePeople.append(personne)
        else:
            print("Le bus est plein")

    def viderUnePersonne(self):
        if self.nbPersonnes != 0:
            self.nbPersonnes -= 1
            self.listePeople.remove(self.listePeople[0])
            return self.listePeople[0]
        else:
            print("Le bus est vide")

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getDistanceFromNextStop(self):
        return self.distanceFromNextStop

    def getNextStation(self):
        if self.travel.index(self.position) == len(self.travel) - 1:
            self.travel.reverse()
        else:
            return self.travel[self.travel.index(self.position) + 1]

    def setDistanceFromNextStop(self):
        if self.distanceFromNextStop > 0:
            self.distanceFromNextStop -= 1
        else:
            self.distanceFromNextStop = self.getNextStation()

    def getPeople(self):
        return self.listePeople

    def addPeople(self, people):
        self.listePeople.append(people)
