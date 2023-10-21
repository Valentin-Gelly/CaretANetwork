import time

from .road import Road
from .stop import Stop
from .people import People
from .travel import Travel


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
        self.allStepRaod = []
        self.terminus = self.travel[-1]
        self.retour = False
        self.stepPassed = []
        self.nbStep = 0


    def __str__(self):
        return 'bus de ' + str(
            self.nbPersonnes) + ' personnes, qui réalise le trajet ' + str(self.allStepRaod) + ' à une vitesse de ' + str(
            self.speedMetter)+'/' + str(self.speedTime) + ', il met ' + str(
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
        if self.nbPersonnes != self.nbPlace:
            self.nbPersonnes += 1
            self.listePeople.append(personne)
            return personne
        else:
            print("Le bus est plein")

    def viderUnePersonne(self, people):
        if self.nbPersonnes != 0:
            if people.voyageActuel.getTravel()[1] == self.getPosition():
                self.nbPersonnes -= 1
                self.listePeople.remove(people)
                time.sleep(1)
                return people
        else:
            print("Le bus est vide")

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getDistanceFromNextStop(self):
        return self.distanceFromNextStop


    def setDistanceFromNextStop(self):
        if self.distanceFromNextStop > 0:
            self.distanceFromNextStop -= 1
        else:
            self.distanceFromNextStop = self.getNextStation()

    def getPeople(self):
        return self.listePeople

    def addPeople(self, people):
        self.listePeople.append(people)

    def isNotFull(self):
        return self.nbPersonnes != self.nbPlace

    def getnbPlaces(self):
        return self.nbPlace

    def getStrTravel(self):
        text=""
        for stop in self.travel:
            text+=stop+" -> "
        return text

    def getNextStep(self):
        for step in self.allStepRaod[len(self.stepPassed):]:
            if step[0] == self.position:
                return step


    def getAllStepStr(self):
        text=""
        for step in self.allStepRaod:
            text+=step[0]+" -> "
        return text


    def getAllPeopleInBus(self):
        text=""
        for people in self.listePeople:
            text+=people.getNom()+", "
        return text

    def getStateBus(self):
        text = ""
        for people in self.listePeople:
            text += people.getNom() + ", "
        if len(self.position)!=1 :
            print( "Bus de la ligne ", self.getStrTravel(), " qui est à la route ", self.getPosition(), " avec ", self.getNbPersonnes(), " personnes : ", text)
        else:
            print("Bus de la ligne ", self.getStrTravel(), " qui est à l'arrêt ", self.getPosition(), " avec ", self.getNbPersonnes(), " personnes : ", text)
