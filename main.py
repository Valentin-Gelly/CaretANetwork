import time
import heapq
import threading

from Classes.bus import Bus
from Classes.stop import Stop
from Classes.road import Road
from Classes.people import People
from Classes.travel import Travel

listeRoute = []
listeRoute.append(Road('A', 'B', 10))
listeRoute.append(Road('A', 'C', 4))
listeRoute.append(Road('C', 'D', 12))
listeRoute.append(Road('C', 'E', 4))

dicRoad = {}

for road in listeRoute:
    if road.start not in dicRoad:
        dicRoad[road.start] = []
        dicRoad[road.start].append({road.stop: road.distance})
    else:
        dicRoad[road.start].append({road.stop: road.distance})
for road in listeRoute:
    if road.stop not in dicRoad:
        dicRoad[road.stop] = []
        dicRoad[road.stop].append({road.start: road.distance})
    else:
        dicRoad[road.stop].append({road.start: road.distance})

dicRoad2 = dicRoad
print('dic2', dicRoad2)

listeBus = []
listeBus.append(Bus(10, 1, [1, 30], 'BACECA'))
listeBus.append(Bus(10, 1, [1, 30], 'DCEC'))
listeBus.append(Bus(10, 1, [1, 30], 'BED'))
listeBus.append(Bus(2, 1, [1, 10], 'AC'))

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


def getIndexRoad(start, stop) -> Road:
    if start in dicRoad:
        for road in dicRoad[start]:
            if stop in road:
                return road[stop]


def dijkstra(graph2, start, end):
    graph = graph2
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # print("graph", graph)
    priority_queue = [(0, start)]
    previous_nodes = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor_info in graph[current_node]:
            # print("neighbor_info", neighbor_info)
            neighbor_info_copy = dict(neighbor_info)
            neighbor, weight = neighbor_info_copy.popitem()
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    while end:
        path.insert(0, end)
        end = previous_nodes.get(end, None)

    return path


for y, bus in enumerate(listeBus):
    for x, stop in enumerate(bus.travel):
        graph = dicRoad2
        if x + 1 < len(bus.travel):
            Parcours = dijkstra(graph, bus.travel[x], bus.travel[x + 1])

            listeEtape = [Parcours[i] + Parcours[i + 1] for i in range(len(Parcours) - 1)]
            for step in listeEtape:
                bus.allStepRaod.append(step)
                bus.nbStep += 1
    print(bus.getStrTravel(), "bus.allStepRaod ", bus.allStepRaod, ' nbStep : ', bus.nbStep)


def getIndexStop(nameStop):
    for stop in listeStop:
        if stop.startRoads == nameStop:
            return listeStop.index(stop)


def fillBus(bus, x):
    try:
        print(bus.travel.index(listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0].voyageActuel.travel[1]),
              'and', int(listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0].voyageActuel.hour))
        if bus.travel.index(
                listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0].voyageActuel.travel[1]) != -1 and int(
                listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0].voyageActuel.hour) <= horloge:
            # print(listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0].nom + ' trajet  : ' +listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0].voyageAller.travel)
            # print('le bus n°' + str(x + 1) + ', au niveau de  : ' + bus.getPosition() + ', a  ' + str(
            # bus.getNbPersonnes()) + ' passagé(e)(s) : ', bus.remplirUnePersonne(listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0]).nom)
            bus.remplirUnePersonne(listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0])
            listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0].setPosition(bus.getPosition())
            listeStop[getIndexStop(bus.getPosition())].removePeople(
                listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0])

            # time.sleep(bus.timeReload)

    except ValueError:
        null = 0


def unFillBus(bus, x):
    try:
        if len(bus.getPeople()) > 0:
            y = 0
            # print(listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0].nom + ' trajet  : ' +listeStop[getIndexStop(bus.getPosition())].getWaitingQueue()[0].voyageAller.travel)
            for people in bus.getPeople():
                if people.voyageActuel.getTravel()[1] == bus.getPosition():
                    bus.viderUnePersonne(people)
                    people.changeVoyageActuel()
                    listeStop[getIndexStop(bus.getPosition())].addPeople(people)
                    # print('le bus n°' + str(x + 1) + ', au niveau de  : ' + bus.getPosition() + ', a  ' + str(
                    # bus.getNbPersonnes()) + ' passagé(e)(s)')

                return people

    except ValueError:
        null = 0


def peopleWantTakeBus(bus, x):
    try:
        if listeStop[getIndexStop(bus.getPosition())].getWaitingQueue() != []:
            for people in listeStop[getIndexStop(bus.getPosition())].getWaitingQueue():
                # print(listeStop[getIndexStop(bus.getPosition())].getWaitingQueue())
                if people.voyageActuel.getTravel()[1] in bus.travel and int(people.voyageActuel.hour) <= horloge:
                    # print(people.nom + ' veut prendre le bus')
                    return True
                else:
                    return False
    except IndexError:
        null = 0


def peopleWantTakeDown(bus, x):
    try:
        if bus.getPeople():
            for people in bus.getPeople():
                if people.voyageActuel.getTravel()[1] == bus.getPosition():
                    return True
                else:
                    return False
    except IndexError:
        null = 0


def busIsInStop(bus, x):
    #
    # Le bus est à l'arret et voit si du monde veut descendre
    #

    if len(bus.getPosition()) == 1 and peopleWantTakeDown(bus, x):
        # print("quelqu'un descend du bus : ", unFillBus(bus, x).nom)
        unFillBus(bus, x)
    #
    # le bus est plein à un arret
    #
    elif len(bus.getPosition()) == 1 and bus.getNbPersonnes() == bus.nbPlace:
        # print("Le bus n°" + str(x + 1) + " est plein")
        bus.setPosition(bus.getNextStep())
        for people in bus.getPeople():
            people.setPosition(bus.getPosition())

    #
    # le bus n'est pas plein et il y a des personnes à l'arrêt
    #

    elif len(bus.getPosition()) == 1 and listeStop[getIndexStop(
            bus.getPosition())].getWaitingQueue() != [] and bus.getNbPersonnes() != bus.nbPlace and peopleWantTakeBus(
            bus, x):
        # print("Le bus n°" + str(x + 1) + " n'est pas complet et il y a des personnes à l'arrêt " + bus.getPosition())
        # print(bus.allStepRaod)
        text = ""
        for people in listeStop[getIndexStop(bus.getPosition())].getWaitingQueue():
            text += str(people.voyageActuel) + ", "
        print(text)
        fillBus(bus, x)

    #
    # le bus n'est pas plein et il n'y a personne à l'arrêt
    #

    elif len(bus.getPosition()) == 1 and listeStop[getIndexStop(bus.getPosition())].getWaitingQueue() == []:
        # print("Le bus n°" + str(x + 1) + " n'est pas complet et il n'y a personne à l'arrêt" + bus.getPosition())
        bus.setPosition(bus.getNextStep())
        # print("Le bus n°" + str(x + 1) + " est au niveau de " + str(bus.getPosition()))
        bus.distanceFromNextStop += bus.speedMetter
        for people in bus.getPeople():
            people.setPosition(bus.getPosition())

    #
    # le bus est vide et personne ne veut monter
    #
    elif len(bus.getPosition()) == 1 and bus.position != bus.travel[len(bus.travel) - 1] and listeStop[getIndexStop(
            bus.getPosition())].getWaitingQueue() != [] and bus.getNbPersonnes() != bus.nbPlace and not peopleWantTakeBus(
            bus, x):
        # print("Le bus n°" + str(x + 1) + " est vide et personne ne veut monter ", bus.position)
        bus.setPosition(bus.getNextStep())


    #
    # le bus est au niveau d'un arrêt mais pas au terminus
    #
    elif len(bus.getPosition()) == 1 and bus.nbStep != len(bus.stepPassed):
        # print("Test Le bus n°" + str(x + 1) + " est au niveau de " + bus.getPosition())
        bus.setPosition(bus.getNextStep())
        for people in bus.getPeople():
            people.setPosition(bus.getPosition())
        if len(bus.getPeople()) > 0:
            unFillBus(bus, x)


    #
    # le bus est en route
    #
    elif len(bus.getPosition()) == 2 and bus.distanceFromNextStop != getIndexRoad(bus.getPosition()[0],
                                                                                  bus.getPosition()[1]):
        # print("Le bus n°" + str(x + 1) + " est au niveau de " + bus.getPosition() + " et est à " + str(bus.getDistanceFromNextStop()),"/",getIndexRoad(bus.getPosition()[0],bus.getPosition()[1]))
        bus.distanceFromNextStop += bus.speedMetter

    #
    # le bus est au niveau de l'arrêt suivant soit il est au terminus soit il est juste à un arret
    #
    elif len(bus.getPosition()) == 2 and bus.distanceFromNextStop == getIndexRoad(bus.getPosition()[0],
                                                                                  bus.getPosition()[1]):
        bus.stepPassed.append(bus.getPosition())
        # print(bus.travel , 'bus stepPassed : ', bus.stepPassed ,"/", bus.nbStep, '/', len(bus.stepPassed))
        if bus.getPosition()[1] == bus.terminus and bus.nbStep == len(bus.stepPassed):
            # print("Le bus n°" + str(x + 1) + " est au terminus")
            bus.distanceFromNextStop = 0

            bus.setPosition(bus.getPosition()[1])
            for people in bus.getPeople():
                people.setPosition(bus.getPosition())

            if len(bus.getPeople()) > 0:
                unFillBus(bus, x)

            bus.allStepRaod = bus.allStepRaod[::-1]
            for y, step in enumerate(bus.allStepRaod):
                bus.allStepRaod[y] = step[::-1]
            bus.travel = bus.travel[::-1]
            bus.terminus = bus.travel[bus.travel.index(bus.terminus) - 1]
            bus.stepPassed = []
        else:
            # print("Le bus n°" + str(x + 1) + " est au niveau de l'arret " + bus.getPosition()[1])
            bus.distanceFromNextStop = 0
            bus.setPosition(bus.getPosition()[1])
            for people in bus.getPeople():
                people.setPosition(bus.getPosition())
            if len(bus.getPeople()) > 0 and peopleWantTakeDown(bus, x):
                unFillBus(bus, x)


horloge = 0

while True:
    print("--------------------------------------------------")
    print("tempo : ", horloge)
    for x, bus in enumerate(listeBus):
        if bus.speedTime == 30:
            if bus.speedTime % 30 == 0:
                busIsInStop(bus, x)
        else:
            if bus.speedTime % 10 == 0:
                busIsInStop(bus, x)
    horloge += 1
    print('\n')
    print('\n')
    for bus in listeBus:
        bus.getStateBus(dicRoad)
    print('\n')
    print('\n')
    for stop in listeStop:
        stop.getStopState()

    print("--------------------------------------------------")
    print('\n')
    time.sleep(1)
