from customtkinter import *

principal = "#52A5E0"
titulo_color = "#EFF3F5"        #Se suele usar para los titulos y el texto en los botones
texto_color = "#C8CDD0"         #Para los parrafos de texto
subtitulo_color = "#A0A7AC"     #Para los subtitulos
borde_color = "#2A3B47"         #Para el borde de los widgets y para el color del hover
contenedor_color = "#212E36"    #Para el color del frame principal
cuerpo_color = "#192229"        #Para los frames secundarios

class Vista_Explorar(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color=contenedor_color)
        self.parent = parent
        self.controlador = controlador

        #Posición en la App
        self.pack(expand=True, fill="both", padx=2, pady=2)

        #Grid Layout
        self.rowconfigure((0,1,3), weight=1, uniform="a")
        self.rowconfigure((2), weight=7, uniform="a")
        self.columnconfigure((0,1,2,3,4), weight=1, uniform="a")

        #Widgets
        self.crear_widgets()
        self.posicion_widgets()

    #Creación de widgets
    def crear_widgets(self):
        #Botones
        self.boton_volver = CTkButton(self, text="",
                                      width=70, height=30,
                                      border_width=2,
                                      fg_color=cuerpo_color,
                                      border_color=borde_color,
                                      hover_color=borde_color,
                                      text_color= titulo_color,
                                      font=("Open Sans",15),
                                      image=self.parent.cargar_icono("home.png"),
                                      command=self.controlador.volver)
        self.boton_filtrar = CTkButton(self, text="",
                                       width=70, height=30,
                                       border_width=2,
                                       fg_color=cuerpo_color,
                                       border_color=borde_color,
                                       hover_color=borde_color,
                                       text_color= titulo_color,
                                       font=("Open Sans",15),
                                       image=self.parent.cargar_icono("buscar.jpg"),
                                       command=lambda: self.controlador.filtrar(self.tipo_filtro_var.get(),
                                                                                self.valor_a_buscar_var.get()))
        self.boton_quitar_filtro = CTkButton(self, text="Quitar filtro", 
                                             height=35, border_width=2,
                                             fg_color=cuerpo_color,
                                             border_color=borde_color,
                                             text_color= titulo_color,
                                             font=("Open Sans",15),
                                             command=self.controlador.quitar_filtro)

        #Etiquetas
        self.titulo_eventos = CTkLabel(self, text="Eventos",
                                       text_color=principal, 
                                       font=("Roboto", 30, "bold"))
        self.filtrar_etiqueta = CTkLabel(self, text="Filtrar por:",
                                         text_color=titulo_color, 
                                         font=("Roboto", 15, "bold"))
        
        #Variable de contról
        self.tipo_filtro_var = StringVar(value="Artista")
        self.valor_a_buscar_var = StringVar(value="Ghost")


        #Option_Menu
        self.tipo_filtro_option = CTkOptionMenu(self, values=["Artista", "Genero"], variable=self.tipo_filtro_var, command=self.cambiar_filtro,
                                                fg_color=cuerpo_color, 
                                                button_color=contenedor_color,
                                                button_hover_color=borde_color,
                                                dropdown_fg_color=contenedor_color,
                                                dropdown_hover_color=borde_color,
                                                dropdown_text_color=titulo_color,
                                                text_color=titulo_color)
        self.artista_option = CTkOptionMenu(self, values=["Ghost", "Luis Miguel", "Pedro Capo"], variable=self.valor_a_buscar_var,
                                            fg_color=cuerpo_color, 
                                            button_color=contenedor_color,
                                            button_hover_color=borde_color,
                                            dropdown_fg_color=contenedor_color,
                                            dropdown_hover_color=borde_color,
                                            dropdown_text_color=titulo_color,
                                            text_color=titulo_color)
        self.genero_option = CTkOptionMenu(self, values=["Arena rock", "Balada", "Bolero", "Dance-Pop", "Doom metal", 
                                                         "Hard rock", "Heavy metal", "Mariachi", "Pop latino", "Pop rock", 
                                                         "Rock progresivo", "Rock psicodelico"], variable=self.valor_a_buscar_var,
                                                         fg_color=cuerpo_color, 
                                                         button_color=contenedor_color,
                                                         button_hover_color=borde_color,
                                                         dropdown_fg_color=contenedor_color,
                                                         dropdown_hover_color=borde_color,
                                                         dropdown_text_color=titulo_color,
                                                         text_color=titulo_color)

    #Posición de widgets
    def posicion_widgets(self):
        self.boton_volver.grid(row=3, column=2, padx=5, pady=5)
        self.boton_filtrar.grid(row=1, column=3, padx=5, pady=5)
        self.boton_quitar_filtro.grid(row=1, column=4, padx=5, pady=5)
        self.titulo_eventos.grid(row=0, column=2, padx=5, pady=5)
        self.filtrar_etiqueta.grid(row=1, column=0, padx=5, pady=5)
        self.tipo_filtro_option.grid(row=1, column=1, padx=5, pady=5)
        self.genero_option.grid(row=1, column=2, padx=5, pady=5)
        self.artista_option.grid(row=1, column=2, padx=5, pady=5)
        self.artista_option.tkraise()

    def cambiar_filtro(self, choice):
        print(choice)
        if choice == "Artista":
            self.artista_option.tkraise()
            self.valor_a_buscar_var.set(value="Ghost")
        else:
            self.genero_option.tkraise()
            self.valor_a_buscar_var.set(value="Arena rock")
