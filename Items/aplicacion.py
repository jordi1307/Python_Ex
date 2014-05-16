__author__ = 'jor'
import Items.Identificador


class Aplicacion(Items.Identificador.Identificador):
    precio = ""
    numero_de_descargas = ""
    numero_de_puntuaciones_obtenidas = ""
    puntuacions = ""
    numero_de_comentarios = ""

    def __init__(self, nombre, proveedor, fecha_publicacion, precio, numero_de_descargas,
                 numero_de_puntuaciones_obtenidas,
                 puntuacions, numero_de_comentarios):
        super.__init__(nombre, proveedor, fecha_publicacion)
        self.precio = precio
        self.numero_de_descargas = numero_de_descargas
        self.numero_de_puntuaciones_obtenidas = numero_de_puntuaciones_obtenidas
        self.puntuacions = puntuacions
        self.numero_de_comentarios = numero_de_comentarios


    def get_precio(self):
        return self.precio
        return self.numero_de_descargas

    def get_numero_de_puntuaciones_obtenidas(self):
        return self.numero_de_puntuaciones_obtenidas

    def get_puntuacions(self):
        return self.puntuacions

    def get_numero_de_comentarios(self):
        return self.numero_de_comentarios


    def set_precio(self, precio):
        self.precio = precio

    def set_numero_de_descargas(self, numero_de_descargas):
        self.numero_de_descargas = numero_de_descargas

    def set_numero_de_puntuaciones_obtenidas(self, numero_de_puntuaciones_obtenidas):
        self.numero_de_puntuaciones_obtenidas = numero_de_puntuaciones_obtenidas

    def set_puntuacions(self, puntuacions):
        self.puntuacions = puntuacions

    def set_numero_de_comentarios(self, numero_de_comentarios):
        self.numero_de_comentarios = numero_de_comentarios

    #auxiliar
    def To_setring_seif(self):
        linea = str(self.get_nombre()) + ":"
        linea += str(self.get_Proveedor()) + ":"
        linea += str(self.get_fecha_publicacion()) + ":"
        linea += set(self.get_precio()) + ":"
        linea += set(self.get_numero_de_descargas()) + ":"
        linea += set(self.get_numero_de_puntuaciones_obtenidas) + ":"
        linea += set(self.get_puntuacions) + ":"
        linea += set(self.get_numero_de_comentarios)
        return linea

    def posicion(self):
        return abs(float(self.get_numero_de_descargas()) * 0.6 + float(self.get_puntuacions()) * 0.25 + float(
            self.get_numero_de_comentarios()) * 0.25)

    def set_seif(self):
        with open("C:\\Users\jor\Desktop\DAM\DAM2\phyton\Python\proyecto-pycharm\Python_Ex\BBDD\\aplicaciones.txt",
                  mode='a', encoding='utf-8') as contingut:
            contingut.writelines(str(self.To_setring_seif()))

