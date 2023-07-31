from customtkinter import *

class Controlador_Detalles:
    def __init__(self, app, evento_seleccionado):
        self.app = app
        self.evento_seleccionado = evento_seleccionado

    def mostrar_seccion_ubicacion(self):
        self.app.vista_detalles.destroy()
        self.app.mostrar_ubicacion()

    def volver(self):
        self.app.vista_detalles.destroy()
        self.app.mostrar_explorar()
