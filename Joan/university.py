"""
Creem una clase amb nom: university. Aquesta clase conté un constructor, 6 atributs, getters i setters, i un mètode amb nom
info on es mostren les dades (atributs).
"""
class university:
    def __init__(self, nom, direccio, localitat, telf, codi_postal, capacitat_alumnes):
        self.nom = nom
        self.direccio = direccio
        self.localitat = localitat
        self.telf = telf
        self.codi_postal = codi_postal
        self.capacitat_alumnes = capacitat_alumnes

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getDireccio(self):
        return self.direccio

    def setDireccio(self, direccio):
        self.direccio = direccio

    def getLocalitat(self):
        return self.localitat

    def setcLocalitat(self, localitat):
        self.localitat = localitat

    def getTelf(self):
        return self.telf

    def settTelf(self, telf):
        self.telf = telf

    def getCodi_postal(self):
        return self.codi_postal

    def setCodi_postal(self, codi_postal):
        self.codi_postal = codi_postal

    def getCapacitat_alumnes(self):
        return self.capacitat_alumnes

    def setCapacitat_alumnes(self, capacitat_alumnes):
        self.capacitat_alumnes = capacitat_alumnes

    def info(self):
        print(f"Nom: {self.nom}, direcció i localitat: {self.direccio}, {self.localitat}, telèfon: {self.telf}, codi postal: {self.codi_postal}, capacitat d'alumnes: {self.capacitat_alumnes}.")

