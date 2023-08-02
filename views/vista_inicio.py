from customtkinter import *

principal = "#52A5E0"
titulo_color = "#EFF3F5"        #Se suele usar para los titulos y el texto en los botones
texto_color = "#C8CDD0"         #Para los parrafos de texto
subtitulo_color = "#A0A7AC"     #Para los subtitulos
borde_color = "#2A3B47"         #Para el borde de los widgets y para el color del hover
contenedor_color = "#212E36"    #Para el color del frame principal
cuerpo_color = "#192229"        #Para los frames secundarios

class Vista_Inicio(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color=contenedor_color, border_color=borde_color)
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
                                        fg_color=cuerpo_color,
                                        border_color=contenedor_color,
                                        text_color= titulo_color,
                                        font=("Open Sans",15),
                                        command=self.controlador.mostrar_explorar)
        self.boton_mi_perdil = CTkButton(self, text="Mi Perfil", 
                                         fg_color=cuerpo_color,
                                         border_color=contenedor_color,
                                         text_color= titulo_color,
                                         font=("Open Sans",15),
                                         command=lambda: self.controlador.mi_perfil(self.parent.usuarios[-1].id))
        self.boton_salir = CTkButton(master=self, text="Salír", 
                                     fg_color=cuerpo_color,
                                     border_color=contenedor_color,
                                     text_color= titulo_color,
                                     font=("Open Sans",15),
                                     command=self.controlador.salir)

    #Posicón de widgets
    def posición_widgets(self):
        self.boton_explorar.grid(row=1, column=0, padx=5, pady=5)
        self.boton_mi_perdil.grid(row=2, column=0, padx=5, pady=5)
        self.boton_salir.grid(row=3, column=0, padx=5, pady=5)