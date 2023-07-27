from customtkinter import *
from views.vista_inicio import Vista_Inicio
from views.vista_eventos import Vista_Eventos
from controllers.controlador_inicio import Controlador_Inicio
from controllers.controlador_eventos import Controlador_Eventos
set_default_color_theme("dark-blue")
set
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
        controlador = Controlador_Inicio(self)
        self.vista_inicio = Vista_Inicio(self, controlador)

    #Destruye la vista inicial y mustra la vista de eventos
    def mostrar_eventos(self):
        self.vista_inicio.destroy()

        controlador = Controlador_Eventos(self)
        self.vista_eventos = Vista_Eventos(self, controlador)

    def volver_inicio(self):
        self.vista_eventos.destroy()
        self.inicializar()

App()
