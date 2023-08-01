from customtkinter import *

class Controlador_Explorar:
    def __init__(self, app):
        self.app = app

    def volver(self):
        self.app.vista_explorar.destroy()
        self.app.mostrar_inicio()