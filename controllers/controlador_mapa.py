from customtkinter import *

class Controlador_Mapa:
    def __init__(self, app, ubicacion_seleccionada):
        self.app = app
        self.ubicacion_seleccionada = ubicacion_seleccionada

    def mostrar_seccion_detalles(self):
        self.app.vista_mapa.destroy()
        self.app.mostrar_detalles()

    def volver(self):
        self.app.vista_mapa.destroy()

        self.app.mostrar_explorar()
