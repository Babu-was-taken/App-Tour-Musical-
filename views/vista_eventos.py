from customtkinter import *

#Cambio de los colores de la interfaz visual
boton= "#E6D884"
borde= "#A1A892"
frame= "#E5E5E5"
titulo= "#2F242C"
texto= "#E6D884"

class Vista_Eventos(CTkScrollableFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.parent = parent
        self.controlador = controlador
        #Posición en la vista Explorar y al buscar y filtrar
        self.grid(row=2, column=0, columnspan=5, sticky="nsew", padx=2, pady=2)
        

    #Crea un frame ubicado dentro del frame desplegable con la info 
    #de un evento
    def crear_vista_para_evento(self, nombre_evento, descripcion, id):

        #Frame en el que se mostrará el evento
        frame_evento = CTkFrame(self, fg_color=frame, border_color=borde)
        
        #Posición que tomará en el frame desplegable
        frame_evento.pack(expand=True, fill="both", padx=2, pady=2)

        #Grid Layout del frame
        frame_evento.rowconfigure((0,1), weight=1, uniform="a")
        frame_evento.columnconfigure((0,2), weight=1, uniform="a")
        frame_evento.columnconfigure((1), weight=2, uniform="a")


        #Widgets
        #Etiquetas
        nombre_evento = CTkLabel(frame_evento, text=nombre_evento,
                                 text_color=titulo,
                                 font=("Roboto",20))
        foto_evento = CTkLabel(frame_evento, image=self.controlador.app.imagenes[id-1])   #Se le resta 1 al id y se lo usa como indice para
        descripcion_etiqueta = CTkLabel(frame_evento, text=descripcion,                   #mostrar la imagen en ese indice de la lista
                                        text_color=titulo,
                                        font=("Roboto",20))                  

        #Botones
        boton_detalles = CTkButton(frame_evento, text="Ver Detalles",
                                   fg_color=boton,
                                   border_color=borde,
                                   text_color= titulo,
                                   font=("Open Sans",15),
                                   command=lambda: self.controlador.ver_detalles(id))

        #Posición
        nombre_evento.grid(row=0, column=1, padx=5, pady=5)
        foto_evento.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
        descripcion_etiqueta.grid(row=1, column=1, padx=5, pady=5)
        boton_detalles.grid(row=1, column=2, padx=5, pady=5)


    #crea un frame para cada evento
    def agregar_eventos(self, eventos_filtrados=None):
        eventos = eventos_filtrados
        if eventos == None:
            eventos = self.controlador.eventos
        for evento in eventos:
            print(evento)
            self.crear_vista_para_evento(evento.nombre, evento.hora_inicio, evento.id)