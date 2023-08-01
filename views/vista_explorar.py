from customtkinter import *

#Cambio de los colores de la interfaz visual
boton= "#E6D884"
borde= "#A1A892"
frame= "#E5E5E5"
titulo= "#2F242C"
texto= "#E6D884"

class Vista_Explorar(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color=frame, border_color=borde)
        self.parent = parent
        self.controlador = controlador

        #Posición en la App
        self.pack(expand=True, fill="both", padx=2, pady=2)

        #Grid Layout
        self.rowconfigure((0,2), weight=1, uniform="a")
        self.rowconfigure((1), weight=7, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")

        #Widgets
        self.crear_widgets()
        self.posicion_widgets()

    #Creación de widgets
    def crear_widgets(self):
        #Botones
        self.boton_volver = CTkButton(self, text="volver",
                                      fg_color=boton,
                                      border_color= borde,
                                      text_color= titulo,
                                      font=("Open Sans",15),
                                      command=self.controlador.volver)
        
        #Etiquetas
        self.titulo_eventos = CTkLabel(self, text="Eventos",
                                       text_color=titulo, 
                                       font=("Roboto", 30, "bold"))

    #Posición de widgets
    def posicion_widgets(self):
        self.boton_volver.grid(row=2, column=0, padx=5, pady=5)
        self.titulo_eventos.grid(row=0, column=0, padx=5, pady=5)