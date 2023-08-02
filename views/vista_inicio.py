from customtkinter import *

#Cambio de los colores de la interfaz visual
boton= "#E6D884"
borde= "#A1A892"
frame= "#E5E5E5"
titulo= "#2F242C"
texto= "#E6D884"

class Vista_Inicio(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color=frame, border_color=borde)
        self.parent = parent
        self.controlador = controlador

        #Posición en la App
        self.pack(expand=True, fill="both", padx=2, pady=2)
        
        #Grid Layout
        self.rowconfigure((0,1,2,3,4), weight=1, uniform="a")
        self.columnconfigure((0), weight=1, uniform="a")

        #Widgets
        self.crear_widgets()
        self.posición_widgets()

    #Creación de widgets
    def crear_widgets(self):
        self.boton_explorar = CTkButton(master=self, text="Explorar",
                                        fg_color=boton,
                                        border_color= borde,
                                        text_color= titulo,
                                        font=("Open Sans",15),
                                        command=self.controlador.mostrar_explorar)
        self.boton_mi_perdil = CTkButton(self, text="Mi Perfil",
                                         font=("Open Sans",15),
                                         command=lambda: self.controlador.mi_perfil(self.parent.usuarios[-1].id))
        self.boton_salir = CTkButton(master=self, text="Salír", 
                                     fg_color=boton,
                                     border_color=borde,
                                     text_color= titulo,
                                     font=("Open Sans",15),
                                     command=self.controlador.salir)

    #Posicón de widgets
    def posición_widgets(self):
        self.boton_explorar.grid(row=1, column=0, padx=5, pady=5)
        self.boton_mi_perdil.grid(row=2, column=0, padx=5, pady=5)
        self.boton_salir.grid(row=3, column=0, padx=5, pady=5)