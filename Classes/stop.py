from .people import People

class Stop :
    def __init__(self, startRoad):
        self.startRoads = startRoad
        self.waitingQueue = []
        self.tempWaitingQueue = 0
        self.tempWaitingQueue2 = 0

    def __str__(self):
        return 'Stop de ' + str(self.startRoads) + ' qui a une queue de ' + str(self.waitingQueue) + " avec "+  str(self.tempWaitingQueue) + " de temps d'attente qui attendent le bus"

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
            text += people.getNom()+ ", "

        print("Arret : ", self.startRoads, " qui a une queue de ", self.getNbPeople(), " personnes : ", text)
        return "Arret : "+ self.startRoads+ " qui a une queue de "+ str(self.getNbPeople())+ " personnes : "+ text + "\n"

    def getTempWaitingQueue(self):
        return self.tempWaitingQueue

    def setTempWaitingQueue(self):
        for people in self.waitingQueue:
            self.tempWaitingQueue += people.getTempsAttente()
        self.tempWaitingQueue= self.tempWaitingQueue/len(self.waitingQueue)
        return self.tempWaitingQueue
    def getTempWaitingQueue2(self):
        return self.tempWaitingQueue2

    def setTempWaitingQueue2(self):
        for people in self.waitingQueue:
            self.tempWaitingQueue2 += people.getTempsAttente()
        self.tempWaitingQueue2= self.tempWaitingQueue2**2
        return self.tempWaitingQueue2


