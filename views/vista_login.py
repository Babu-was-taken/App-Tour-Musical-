from customtkinter import *

principal = "#52A5E0"
titulo_color = "#EFF3F5"        #Se suele usar para los titulos y el texto en los botones
texto_color = "#C8CDD0"         #Para los parrafos de texto
subtitulo_color = "#A0A7AC"     #Para los subtitulos
borde_color = "#2A3B47"         #Para el borde de los widgets y para el color del hover
contenedor_color = "#212E36"    #Para el color del frame principal
cuerpo_color = "#192229"        #Para los frames secundarios

class Vista_Login(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent,fg_color=contenedor_color)
        self.controlador = controlador

        #Posición que tendrá en la App
        self.pack(expand=True, fill="both", padx=2, pady=2)

        #Grid Layout
        self.rowconfigure((0,1,2,3,4,5), weight=1, uniform="a")
        self.columnconfigure((0), weight=1, uniform="a")

        #Widgets
        self.crear_widgets()
        self.posicion_widgets()
    


    def crear_widgets(self):
        #Etiquetas
        self.bienvenido_etiqueta = CTkLabel(self, text="Bienvenido", font=("Open Sans", 25),text_color=titulo_color)

        #Boton
        self.iniciar_sesion_boton = CTkButton(self, height=40, 
                                              text="Iniciar Sesión",
                                              fg_color=cuerpo_color,
                                              border_color= contenedor_color,
                                              text_color= titulo_color,
                                              font=("Open Sans", 20),
                                              command=lambda: 
                                              self.controlador.iniciar_sesion(self.entrada_nombre.get(),
                                                                              self.entrada_apellido.get()))

        #Entradas
        self.entrada_nombre = CTkEntry(self, width=220, height=35, placeholder_text="Nombre")
        self.entrada_apellido = CTkEntry(self, width=220, height=35, placeholder_text="Apellido")

    def posicion_widgets(self):
        self.bienvenido_etiqueta.grid(row=1)
        self.entrada_nombre.grid(row=2)
        self.entrada_apellido.grid(row=3)
        self.iniciar_sesion_boton.grid(row=4)