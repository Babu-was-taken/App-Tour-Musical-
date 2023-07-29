from customtkinter import *
from views.vista_detalles import Vista_Detalles

class Controlador_Detalles:
    def __init__(self, app):
        self.app = app

    def mostrar_seccion_ubicacion(self):
        self.app.vista_detalles.detalles_frame.destroy()
        self.app.vista_detalles.ubicacion_frame.tkraise()

    def mostrar_seccion_detalles(self):
        self.app.vista_detalles.destroy()
        self.app.mostrar_detalles()

    def volver(self):
        self.app.vista_detalles.destroy()
        self.app.mostrar_explorar()