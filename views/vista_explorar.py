from customtkinter import *

class Vista_Explorar(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color="black")
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
        self.boton_volver = CTkButton(self, 
                                      text="volver",fg_color="#E6D884",font=("Open Sans",10),
                                      command=self.controlador.volver,text_color="#2F242C",border_color="#A1A892")
        
        #Etiquetas
        self.titulo_eventos = CTkLabel(self, 
                                       text="Eventos",text_color="#2F242C", 
                                       font=("Roboto", 30, "bold"))

    #Posición de widgets
    def posicion_widgets(self):
        self.boton_volver.grid(row=2, column=0, padx=5, pady=5)
        self.titulo_eventos.grid(row=0, column=0, padx=5, pady=5)