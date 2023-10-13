import time

import threading

from Classes.bus import Bus
from Classes.stop import Stop
from Classes.road import Road
from Classes.people import People
from Classes.travel import Travel

listeBus = []
testBus = Bus(10,  1, [1, 30], 'BACECA')
listeBus.append(testBus)
testBus = Bus(10, 1, [1, 30], 'DCEC')
listeBus.append(testBus)
testBus = Bus(10, 1, [1, 30], 'BED')
listeBus.append(testBus)
testBus = Bus(2, 1, [1, 10], 'AC')

listeRoute = []
listeRoute.append(Road('A', 'B', 10))
listeRoute.append(Road('A', 'C', 4))
listeRoute.append(Road('C', 'D', 12))
listeRoute.append(Road('C', 'E', 4))

listeStop = []
listeStop.append(Stop('A'))
listeStop.append(Stop('B'))
listeStop.append(Stop('C'))
listeStop.append(Stop('D'))
listeStop.append(Stop('E'))

def recupDonnee(nameFile):
    listePeople = []
    with open(nameFile, 'r') as peoples:
        for people in peoples:
            infoPeople = people.split()

            for k in range(int(infoPeople[0])):
                nom = infoPeople[1] + '' + str(k).rjust(2, '0')
                heureDepart = infoPeople[2]
                trajetDepart = infoPeople[3]
                heureRetour = infoPeople[4]
                trajetRetour = infoPeople[5]
                listePeople.append(People(Travel(heureDepart, trajetDepart), Travel(heureRetour, trajetRetour), nom))
    lettreStop = []
    for stop in listeStop:
        lettreStop.append(stop.startRoads)
    for people in listePeople:
        depart = people.voyageAller.travel[0]
        arretDepart = lettreStop.index(depart)
        listeStop[arretDepart].addPeople(people)
    return listePeople


while True:
    try:
        nomChier = input('Nom du fichier des personnes : ')
        listePeople = recupDonnee(nomChier)
        break
    except FileNotFoundError:
        print("Le fichier n'existe pas")
    except ValueError:
        print("Le fichier n'est pas au bon format")

def getIndexStop(nameStop):
    for stop in listeStop:
        if stop.startRoads == nameStop:
            return listeStop.index(stop)


listeThread = []
print(listeStop[1].startRoads)

def fillBus(bus,x):
    try:
        if bus.travel.index(listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0].voyageAller.travel[1]):
            print(listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0].nom + ' trajet  : ' +
                  listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0].voyageAller.travel)
            bus.remplirUnePersonne(listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0])
            listeStop[getIndexStop(bus.getPosition())].removePeople(
                listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0])
            print('le bus n°' + str(x + 1) + ', au niveau de  : ' + bus.getPosition() + ', a  ' + str(
                bus.getNbPersonnes()) + ' passagé(e)(s)')

    except ValueError:
        null = 0




for x,bus in enumerate(listeBus):
    print(bus.travel)
    if len(bus.getPosition()) == 1 and listeStop[getIndexStop(bus.getPosition())].getWaitingQueue() != [] and bus.getNbPersonnes() != bus.nbPlace:
        for i in range(bus.getnbPlaces() - bus.getNbPersonnes()) :
            fillBus(bus,x)
