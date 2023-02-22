class School:
    def __init__(self, nombre, direccion, ciudad, codigo_postal, telefono, num_alumnos):
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.telefono = telefono
        self.num_alumnos = num_alumnos

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_direccion(self):
        return self.direccion

    def get_ciudad(self):
        return self.ciudad

    def get_codigo_postal(self):
        return self.codigo_postal

    def get_telefono(self):
        return self.telefono

    def get_num_alumnos(self):
        return self.num_alumnos

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad

    def set_codigo_postal(self, codigo_postal):
        self.codigo_postal = codigo_postal

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_num_alumnos(self, num_alumnos):
        self.num_alumnos = num_alumnos

    # Método info
    def info(self):
        print(f"El centro de estudios {self.nombre} se encuentra en {self.direccion}, {self.ciudad}, con código postal {self.codigo_postal} y teléfono {self.telefono}. Actualmente tiene {self.num_alumnos} alumnos.")
