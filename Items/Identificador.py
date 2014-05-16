__author__ = 'jor'


class Identificador:
    nombre = ""
    proveedor = ""
    fecha_publicacion = ""

    def __init__(self, nombre, proveedor, fecha_publicacion):
        self.nombre = nombre
        self.proveedor = proveedor
        self.fecha_publicacion = fecha_publicacion

    def get_nombre(self):
        return self.nombre

    def get_Proveedor(self):
        return self.proveedor

    def get_fecha_publicacion(self):
        return self.fecha_publicacion

    def set_Nombre(self, nombre):
        self.nombre = nombre

    def set_Proveedor(self, proveedor):
        self.proveedor = proveedor

    def set_fecha_publicacion(self, fecha_publicacion):
        self.fecha_publicacion = fecha_publicacion


