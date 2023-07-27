from customtkinter import *

class Vista_Eventos(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color="black")
        self.parent = parent
        self.controlador = controlador
        #Posición en la App
        self.pack(expand=True, fill="both")
        #Grid Layout
        self.rowconfigure((0,1,2), weight=1, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")

        self.crear_widgets()
        self.posicion_widgets()

    #Creación de widgets
    def crear_widgets(self):
        #Botones
        self.boton_volver = CTkButton(self, 
                                      text="volver", 
                                      command=self.controlador.volver)
        #Etiquetas
        self.titulo_eventos = CTkLabel(self, 
                                       text="Eventos", 
                                       font=("arial", 30, "bold"))

    #Posición de widgets
    def posicion_widgets(self):
        self.boton_volver.grid(row=2, column=0)
        self.titulo_eventos.grid(row=0, column=0)
