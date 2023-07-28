from customtkinter import *
from PIL import Image, ImageTk
from models.evento import Evento
from views.vista_eventos import Vista_Eventos

class Controlador_Eventos:
    def __init__(self, app, eventos):
        self.app = app
        self.eventos = eventos
        self.imagenes=[]
        self.cargar_imagenes()

    def volver(self):
        self.app.volver_inicio()

    def obtener_eventos(self):
        return self.eventos

    #Añade las imagenes a la lista
    def cargar_imagenes(self):
        for evento in self.eventos:
            imagen = ImageTk.PhotoImage(Image.open(f"assets/{evento.imagen}").resize((200, 200)))
            self.imagenes.append(imagen)

    
