from animal import Animal
from vehicle import Vehicle
from school import School

# Instanciar dos objetos de cada clase creada
mi_animal1 = Animal("Amaranta", 3, "perro", "Shih-Tzu", "blanco", 7)
mi_animal2 = Animal("Ticky", 4, "gato", "Persa", "marrón", 6)
mi_vehiculo1 = Vehicle("Toyota", "Corolla", 2015, "43643757", "azul", 4)
mi_vehiculo2 = Vehicle("Ford", "Fiesta", 2010, "42656545", "blanco", 4)
mi_escuela1 = School("Colegio San Juan", "Calle Mayor 15", "Madrid", "España", 500, 25)
mi_escuela2 = School("Colegio Santa Ana", "Calle París 32", "Barcelona", "España", 300, 20)

# Llamar al método de cada clase para mostrar los resultados
mi_animal1.saludo()
mi_animal2.saludo()
mi_vehiculo1.parts()
mi_vehiculo2.parts()
mi_escuela1.info()
mi_escuela2.info()

# Modificar un atributo de las instancias creadas y mostramos el resultado
mi_animal1.set_edad(4)
print(f"La nueva edad de {mi_animal1.get_nombre()} es {mi_animal1.get_edad()} años.")

mi_vehiculo1.set_anyo(2016)
print(f"El vehículo {mi_vehiculo1.get_marca()} {mi_vehiculo1.get_modelo()} ahora es del año {mi_vehiculo1.get_anyo()}.")

mi_escuela1.set_num_alumnos(550)
print(f"El colegio {mi_escuela1.get_nombre()} ahora tiene {mi_escuela1.get_num_alumnos()} alumnos.")
