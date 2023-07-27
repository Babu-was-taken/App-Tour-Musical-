from customtkinter import *
from models.evento import Evento
from views.vista_eventos import Vista_Eventos

class Controlador_Eventos:
    def __init__(self, app):
        self.app = app

    def volver(self):
        self.app.volver_inicio()