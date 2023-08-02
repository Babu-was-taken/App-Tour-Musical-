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
        self.columnconfigure((1), weight=2, uniform="a")

        #Widgets
        self.crear_widgets()
        self.posición_widgets()

    #Creación de widgets
    def crear_widgets(self):
        #Etiqueta
        self.fondo = CTkLabel(self, text="", image=self.parent.cargar_fondo("fondo_2.jpg"))

        #Botones
        self.boton_explorar = CTkButton(master=self, text="Explorar", 
                                        fg_color=cuerpo_color,
                                        border_color=contenedor_color,
                                        hover_color=cuerpo_color,
                                        text_color= titulo_color,
                                        font=("Open Sans",15),
                                        command=self.controlador.mostrar_explorar)
        self.boton_mi_perdil = CTkButton(self, text="Mi Perfil", 
                                         fg_color=cuerpo_color,
                                         border_color=contenedor_color,
                                         hover_color=cuerpo_color,
                                         text_color= titulo_color,
                                         font=("Open Sans",15),
                                         command=lambda: self.controlador.mi_perfil(self.parent.usuarios[-1].id))
        self.boton_salir = CTkButton(master=self, text="Salír", 
                                     fg_color=cuerpo_color,
                                     border_color=contenedor_color,
                                     hover_color=cuerpo_color,
                                     text_color= titulo_color,
                                     font=("Open Sans",15),
                                     command=self.controlador.salir)

    #Posicón de widgets
    def posición_widgets(self):
        self.fondo.grid(row=0, column=0, rowspan=5, columnspan=2, padx=2, pady=2)
        self.boton_explorar.grid(row=2, column=0, sticky="n", padx=5, pady=5)
        self.boton_mi_perdil.grid(row=3, column=0, sticky="n", padx=5, pady=5)
        self.boton_salir.grid(row=4, column=0, sticky="n", padx=5, pady=5)