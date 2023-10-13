from .travel import Travel

class People:

    def __init__(self, voyageAller:Travel, voyageRetour:Travel, nom):
        self.voyageAller=voyageAller
        self.voyageRetour=voyageRetour
        self.nom = nom
        self.position = voyageAller.travel[0]

    def __str__(self):
        return self.nom +' '+ self.voyageAller.__str__() + ' ' + self.voyageRetour.__str__()

    def getVoyageAller(self):
        return self.voyageAller

    def getVoyageRetour(self):
        return self.voyageRetour

    def getNom(self):
        return self.nom

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getVoyage(self):
        return self.voyageAller.travel + self.voyageRetour.travel





