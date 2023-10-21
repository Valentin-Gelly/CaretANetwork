from .people import People

class Stop :
    def __init__(self, startRoad):
        self.startRoads = startRoad
        self.waitingQueue = []

    def __str__(self):
        return 'Stop de ' + str(self.startRoads) + ' qui a une queue de ' + str(self.waitingQueue)

    def getStartRoads(self):
        return self.startRoads

    def getWaitingQueue(self):
        return self.waitingQueue

    def addPeople(self, people:People):
        self.waitingQueue.append(people)

    def removePeople(self, people:People):
        self.waitingQueue.remove(people)

    def getPeople(self):
        return self.waitingQueue

    def getNbPeople(self):
        return len(self.waitingQueue)

    def getAllPeopleInStop(self):
        text=""
        for people in self.waitingQueue:
            text+=people.getNom()+", "
        return text

    def getStopState(self):
        text = ""
        for people in self.waitingQueue:
            text += people.getNom() + " (travel = "+ str(people.voyageActuel)+")"

        print("Arret : ", self.startRoads, " qui a une queue de ", self.getNbPeople(), " personnes : ", text)
