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
        self.frame_enviar_comentario = CTkFrame(self, fg_color="black")
        #Grid Layout
        self.frame_enviar_comentario.rowconfigure((0,1,2), weight=1, uniform="a")
        self.frame_enviar_comentario.columnconfigure((0,1,2), weight=1, uniform="a")


        #Etiquetas
        self.comentarios_titulo = CTkLabel(self.frame_enviar_comentario, text="Deja un comentario", font=("Roboto", 15),texto_color=titulo)

        #Entrada
        self.entrada_comentario = CTkEntry(self.frame_enviar_comentario, width=400, placeholder_text="Escribir comentario", font=("Open Sans",10),text_color=texto) 

    def posicion_widgets(self):
        self.frame_enviar_comentario.pack(expand=True, fill="x", padx=2, pady=2)

        self.comentarios_titulo.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.entrada_comentario.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)

    #Crea un frame que contenga un comentario
    def crear_vista_de_comentario(self, usuario, calificacion, animo, comentario):
        frame_comentario = CTkFrame(self, fg_color="black")
        frame_comentario.pack(expand=True, fill="x", padx=2, pady=2)

        #Grid Layout
        frame_comentario.rowconfigure((0,1,2), weight=1, uniform="a")
        frame_comentario.columnconfigure((0,1,2), weight=1, uniform="a")

        #Widgets
        #Etiquetas
        comentario_usuario = CTkLabel(frame_comentario, text=usuario,font=("Open Sans", 10),texto_color=texto)
        comentario_calificacion = CTkLabel(frame_comentario, text=f"Nota: {calificacion}/5",font=("Open Sans", 10),texto_color=texto)
        comentario_animo = CTkLabel(frame_comentario, text=animo,font=("Open Sans", 10),texto_color=texto)
        comentario_comentario = CTkLabel(frame_comentario, text=comentario,font=("Open Sans", 10),texto_color=texto)

        #Posición
        comentario_usuario.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        comentario_calificacion.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        comentario_animo.grid(row=1, column=0, padx=5, pady=5)
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