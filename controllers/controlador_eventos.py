from customtkinter import *
from PIL import Image, ImageTk

class Controlador_Eventos:
    def __init__(self, app, eventos):
        self.app = app

        self.eventos = eventos

    def obtener_eventos(self):
        return self.eventos

    def ver_detalles(self, id):
        self.app.vista_explorar.destroy()
        self.app.seleccionar_evento(id)
        self.app.mostrar_detalles()


