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
        self.rowconfigure((0,1,3), weight=1, uniform="a")
        self.rowconfigure((2), weight=7, uniform="a")
        self.columnconfigure((0,1,2,3,4), weight=1, uniform="a")

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
        self.boton_filtrar = CTkButton(self, text="Filtrar", 
                                       font=("Open Sans",15),
                                       command=lambda: self.controlador.filtrar(self.tipo_filtro_var.get(),
                                                                                self.valor_a_buscar_var.get()))
        self.boton_quitar_filtro = CTkButton(self, text="Quitar filtro",
                                             fg_color="orange",
                                             font=("Open Sans",15),
                                             command=self.controlador.quitar_filtro)

        #Etiquetas
        self.titulo_eventos = CTkLabel(self, text="Eventos",
                                       text_color=titulo, 
                                       font=("Roboto", 30, "bold"))
        self.filtrar_etiqueta = CTkLabel(self, text="Filtrar por:",
                                         text_color=titulo, 
                                         font=("Roboto", 15, "bold"))
        
        #Variable de contról
        self.tipo_filtro_var = StringVar(value="Artista")
        self.valor_a_buscar_var = StringVar(value="Ghost")


        #Option_Menu
        self.tipo_filtro_option = CTkOptionMenu(self, values=["Artista", "Genero"], variable=self.tipo_filtro_var, command=self.cambiar_filtro)
        self.artista_option = CTkOptionMenu(self, values=["Ghost", "Luis Miguel", "Pedro Capo"], variable=self.valor_a_buscar_var)
        self.genero_option = CTkOptionMenu(self, values=["Arena rock", "Balada", "Bolero", "Dance-Pop", "Doom metal", 
                                                         "Hard rock", "Heavy metal", "Mariachi", "Pop latino", "Pop rock", 
                                                         "Rock progresivo", "Rock psicodelico"], variable=self.valor_a_buscar_var)

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
            self.valor_a_buscar_var.set(value="Ghos")
        else:
            self.genero_option.tkraise()
            self.valor_a_buscar_var.set(value="Arena rock")
