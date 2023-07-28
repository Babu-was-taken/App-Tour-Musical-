from customtkinter import *
from models.evento import Evento
from views.vista_inicio import Vista_Inicio
from views.vista_explorar import Vista_Explorar
from views.vista_eventos import Vista_Eventos
from controllers.controlador_inicio import Controlador_Inicio
from controllers.controlador_explorar import Controlador_Explorar
from controllers.controlador_eventos import Controlador_Eventos

set_default_color_theme("dark-blue")

class App(CTk):
    def __init__(self):
        super().__init__()
        #Setup principal
        self.title("App Tour Musical 0.1")
        self.geometry("600x400")
        self.minsize(600,400)

        #Inicializar
        self.inicializar()

        #Run 
        self.mainloop()

    def inicializar(self):
        #Se cargan los eventos
        eventos = Evento.cargar_de_json("data/evento.json")

        #Se cargan los controladores y se les asigna la lista de eventos
        self.controlador_inicio = Controlador_Inicio(self)
        self.controlador_explorar = Controlador_Explorar(self)
        self.Controlador_eventos = Controlador_Eventos(self, eventos)

        #Se muestra la pantalla inicial
        self.vista_inicio = Vista_Inicio(self, self.controlador_inicio)

    #Destruye la vista inicial y mustra la vista de eexplorar con los eventos cargados
    def mostrar_explorar(self):
        self.vista_inicio.destroy()

        self.vista_explorar = Vista_Explorar(self, self.controlador_explorar)
        self.vista_eventos = Vista_Eventos(self.vista_explorar, self.Controlador_eventos)
        
    def volver_inicio(self):
        self.vista_explorar.destroy()
        self.inicializar()



App()
