from customtkinter import *
from tkinter.messagebox import *

class Controlador_Inicio:
    def __init__(self, app):
        self.app = app

    def mostrar_explorar(self):
        self.app.vista_inicio.destroy()
        self.app.mostrar_explorar()

    def salir(self):
        respuesta = askyesno("Confirmar", "¿Seguro que desea salír?")
        if respuesta:
            self.app.destroy()

