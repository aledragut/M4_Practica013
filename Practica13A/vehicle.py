class Vehicle:
    def __init__(self, marca, modelo, anyo, matricula, color, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.anyo = anyo
        self.matricula = matricula
        self.color = color
        self.num_ruedas = num_ruedas

    # Getters
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_anyo(self):
        return self.anyo

    def get_matricula(self):
        return self.matricula

    def get_color(self):
        return self.color

    def get_num_ruedas(self):
        return self.num_ruedas

    # Setters
    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_anyo(self, anyo):
        self.anyo = anyo

    def set_matricula(self, matricula):
        self.matricula = matricula

    def set_color(self, color):
        self.color = color

    def set_num_ruedas(self, num_ruedas):
        self.num_ruedas = num_ruedas

    # Método parts
    def parts(self):
        print(f"Este es un {self.marca} {self.modelo} del año {self.anyo} con matrícula {self.matricula}. Es de color {self.color} y tiene {self.num_ruedas} ruedas.")


