"""
Creem una clase amb nom: book. Aquesta clase conté un constructor, 6 atributs, getters i setters, i un mètode amb nom
info on es mostren les dades (atributs).
"""
class book:
    def __init__(self, nom, autor, genere, npagines, idioma, editorial):
        self.nom = nom
        self.autor = autor
        self.genere = genere
        self.npagines = npagines
        self.idioma = idioma
        self.editorial = editorial

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getAutor(self):
        return self.autor

    def setAutor(self, autor):
        self.autor = autor

    def getGenere(self):
        return self.genere

    def setGenere(self, genere):
        self.genere = genere

    def getNpagines(self):
        return self.npagines

    def setNpagines(self, npagines):
        self.npagines = npagines

    def getIdioma(self):
        return self.idioma

    def setIdioma(self, idioma):
        self.idioma = idioma

    def getEditorial(self):
        return self.editorial

    def setEditorial(self, editorial):
        self.editorial = editorial

    def info(self):
        print(f"El nom del llibre és {self.nom}, l'autor és {self.autor}, és del genere {self.genere}, té {self.npagines} pàgines, està en el idioma {self.idioma}i la seva editorial és {self.editorial}.")

