from customtkinter import *
from PIL import Image, ImageTk
from models.evento import Evento
from views.vista_eventos import Vista_Eventos
from views.vista_explorar import Vista_Explorar
from views.vista_detalles import Vista_Detalles
from controllers.controlador_explorar import Controlador_Explorar
from controllers.controlador_detalles import Controlador_Detalles

class Controlador_Eventos:
    def __init__(self, app, eventos):
        self.app = app

        self.eventos = eventos
        self.imagenes=[]
        self.cargar_imagenes()

    def obtener_eventos(self):
        return self.eventos

    #Añade las imagenes a la lista
    def cargar_imagenes(self):
        for evento in self.eventos:
            imagen = ImageTk.PhotoImage(Image.open(f"assets/{evento.imagen}").resize((200, 200)))
            self.imagenes.append(imagen)

    def ver_detalles(self):
        self.app.mostrar_detalles()
    
