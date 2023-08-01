from customtkinter import *

#Cambio de los colores de la interfaz visual
boton= "#E6D884"
borde= "#A1A892"
frame= "#E5E5E5"
titulo= "#2F242C"
texto= "#E6D884"

class Vista_Comentarios(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.parent = parent
        self.controlador = controlador

        #Posición que tendrá en el frame desplegable en Vista Detalles
        self.pack(expand=True, fill="x", padx=2, pady=2)

        #Widgets
        self.crear_widgets()
        self.posicion_widgets()

        self.agregar_comentarios()

    def crear_widgets(self):
        #Frame en el que el usuario podrá escribir un comentario
        self.frame_enviar_comentario = CTkFrame(self, fg_color=borde)
        #Grid Layout
        self.frame_enviar_comentario.rowconfigure((0,1,2,3), weight=1, uniform="a")
        self.frame_enviar_comentario.columnconfigure((0,1,2), weight=1, uniform="a")

        #Variable de contról
        self.nota_var = StringVar(value="5")
        self.nota_var.set("5")
        self.animo_var = StringVar(value="Positivo")
        self.animo_var.set("Positivo")

        #Combobox
        self.nota_combobox = CTkOptionMenu(self.frame_enviar_comentario, values=["1", "2", "3", "4", "5"], variable=self.nota_var)
        self.animo_combobox = CTkOptionMenu(self.frame_enviar_comentario, values=["Positivo", "Negativo"], variable=self.animo_var)

        #Botones
        self.boton_enviar_comentario = CTkButton(self.frame_enviar_comentario, 
                                                 text="Enviar", command=lambda: 
                                                 self.controlador.enviar_comentario(self.nota_var.get(), 
                                                                                    self.animo_var.get(),
                                                                                    self.entrada_comentario.get()))

        #Etiquetas
        self.comentarios_titulo = CTkLabel(self.frame_enviar_comentario, text="Deja un comentario", text_color=titulo, font=("Roboto", 15))
        self.nota_etiqueta = CTkLabel(self.frame_enviar_comentario, text="Nota")
        self.animo_etiqueta = CTkLabel(self.frame_enviar_comentario, text="Ánimo")

        #Entrada
        self.entrada_comentario = CTkEntry(self.frame_enviar_comentario, width=400, placeholder_text="Escribir comentario", text_color=texto, font=("Open Sans",15)) 

    def posicion_widgets(self):
        self.frame_enviar_comentario.pack(expand=True, fill="x", padx=2, pady=2)

        self.nota_combobox.grid(row=2, column=0, padx=5, pady=5)
        self.animo_combobox.grid(row=2, column=1, padx=5, pady=5)

        self.boton_enviar_comentario.grid(row=3, column=3, padx=5, pady=5)

        self.comentarios_titulo.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.nota_etiqueta.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.animo_etiqueta.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        self.entrada_comentario.grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=5)


    #Crea un frame que contenga un comentario
    def crear_vista_de_comentario(self, usuario, calificacion, animo, comentario):
        frame_comentario = CTkFrame(self, fg_color=borde)
        frame_comentario.pack(expand=True, fill="x", padx=2, pady=2)

        #Grid Layout
        frame_comentario.rowconfigure((0,1,2), weight=1, uniform="a")
        frame_comentario.columnconfigure((0,1,2), weight=1, uniform="a")

        #Widgets
        #Etiquetas
        comentario_usuario = CTkLabel(frame_comentario, text=usuario, text_color=titulo, font=("Open Sans", 15))
        comentario_calificacion = CTkLabel(frame_comentario, text=f"Nota: {calificacion}/5", text_color=texto, font=("Open Sans", 15))
        comentario_animo = CTkLabel(frame_comentario, text=animo, text_color=texto, font=("Open Sans", 15))
        comentario_comentario = CTkLabel(frame_comentario, text=comentario, text_color=texto, font=("Open Sans", 15))

        #Posición
        comentario_usuario.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        comentario_calificacion.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        comentario_animo.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        comentario_comentario.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)


    #Genera frames con los comentarios que tengan el mismo id del evento seleccionado
    #Asigna el usario al comentario que tenga el mismo id_usuario
    def agregar_comentarios(self):
        comentarios = self.controlador.app.comentarios
        usuarios = self.controlador.app.usuarios
        for comentario in comentarios:
            if comentario.id_evento == self.controlador.evento_seleccionado.id:
                for usuario in usuarios:
                    if usuario.id == comentario.id_usuario:
                        self.crear_vista_de_comentario(usuario.nombre, comentario.calificacion, comentario.animo, comentario.comentario)