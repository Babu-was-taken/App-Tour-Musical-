from customtkinter import *
from models.evento import Evento
from views.vista_inicio import Vista_Inicio
from views.vista_explorar import Vista_Explorar
from views.vista_eventos import Vista_Eventos
from views.vista_detalles import Vista_Detalles
from views.vista_mapa import Vista_Mapa
from controllers.controlador_inicio import Controlador_Inicio
from controllers.controlador_explorar import Controlador_Explorar
from controllers.controlador_eventos import Controlador_Eventos
from controllers.controlador_detalles import Controlador_Detalles
from controllers.controlador_mapa import Controlador_Mapa
from models.Ubicacion import Ubicacion

set_default_color_theme("dark-blue")

class App(CTk):
    def __init__(self):
        super().__init__()
        #Setup principal
        self.title("App Tour Musical 0.1")
        self.geometry("700x400")
        self.minsize(600,400)

        #Inicializar
        self.inicializar()

        #Run 
        self.mainloop()

    def inicializar(self):
        #Se cargan los eventos y las ubicaciones
        eventos = Evento.cargar_de_json("data/evento.json")
        self.ubicaciones = Ubicacion.cargar_de_json("data/ubicacion.json")
        print(self.ubicaciones)

        #Se cargan los controladores y se les asigna la lista de eventos
        self.controlador_inicio = Controlador_Inicio(self)
        self.controlador_explorar = Controlador_Explorar(self)
        self.Controlador_eventos = Controlador_Eventos(self, eventos)
        self.controlador_detalles = Controlador_Detalles(self)
        self.controlador_mapa = Controlador_Mapa(self)

        #Se muestra la pantalla inicial
        self.mostrar_inicio()


    #Mostrar vistas
    def mostrar_inicio(self):
        self.vista_inicio = Vista_Inicio(self, self.controlador_inicio)

    def mostrar_explorar(self):
        self.vista_explorar = Vista_Explorar(self, self.controlador_explorar)
        self.vista_eventos = Vista_Eventos(self.vista_explorar, self.Controlador_eventos)

    def mostrar_detalles(self):
        self.vista_explorar.destroy()
        self.vista_eventos.destroy()

        self.vista_detalles = Vista_Detalles(self, self.controlador_detalles)
        self.vista_mapa = Vista_Mapa(self.vista_detalles.ubicacion_frame, self.controlador_mapa)

        self.vista_detalles.detalles_frame.tkraise()



App()

