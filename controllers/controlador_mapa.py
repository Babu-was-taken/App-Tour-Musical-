from customtkinter import *

class Controlador_Mapa:
    def __init__(self, app):
        self.app = app
        self.marcadores = []

"""
        self.cargar_marcadores()


    def agregar_marcador_mapa(self, latitud, longitud):
        return self.app.vista_mapa.mapa.set_marker(latitud, longitud)


    def cargar_marcadores(self):
        for ubicacion in self.app.ubicaciones:
            print(ubicacion.latitud, ubicacion.longitud)
            self.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud)"""