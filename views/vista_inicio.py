from customtkinter import *

class Vista_Inicio(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color="black")
        self.parent = parent
        self.controlador = controlador

        #Posición en la App
        self.pack(expand=True, fill="both", padx=2, pady=2)
        
        #Grid Layout
        self.rowconfigure((0,1), weight=1, uniform="a")
        self.columnconfigure((0), weight=1, uniform="a")

        #Widgets
        self.crear_widgets()
        self.posición_widgets()

    #Creación de widgets
    def crear_widgets(self):
        self.boton_explorar = CTkButton(master=self, 
                                        text="Explorar",
                                        command=self.controlador.mostrar_explorar)
        self.boton_salir = CTkButton(master=self, 
                                     text="Salír",
                                     command=self.controlador.salir)

    #Posicón de widgets
    def posición_widgets(self):
        self.boton_explorar.grid(row=0, column=0, padx=5, pady=5)
        self.boton_salir.grid(row=1, column=0, padx=5, pady=5)