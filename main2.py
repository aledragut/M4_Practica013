from Joan.book import book
from Joan.user import user
from Joan.university import university

b1 = book("I.T.", "Stephen King", "terror", 400, "castellà", "Norma")
b1.info()
b1.setIdioma("Anglès")
b1.info()
b2 = book("El señor de los anillos", "J. R. R. Tolkien", "ficció", 700, "castella", "Kobo")
b2.info()
b2.setEditorial("Planeta")
b2.info()

u1 = user("Joan", "Gago", "joan1234", "joangago8@gmail.com", "Administració", "Administrador")
u1.salutacio()
u1.setNom("Juan")
u1.salutacio()
u2 = user("Anna", "Gago", "anna1234", "annagago8@gmail.com", "Marqueting", "Lectura")
u2.salutacio()
u2.setPermisos("Lectura i escriptura")
u2.salutacio()

uni1 = university("UB", "bac de Roda 79", "Barcelona", "934 02 11 00", "08005", "700")
uni1.info()
uni1.setCapacitat_alumnes("1000")
uni1.info()
uni2 = university("UPC", "Paseig Taulat", "Barcelona", "934 20 12 23", "08005", "500")
uni2.info()
uni2.setNom("UAB")
uni2.info()