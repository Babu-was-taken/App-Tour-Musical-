from customtkinter import *

class Vista_Eventos(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color="black")
        self.parent = parent
        self.controlador = controlador

        #Posición en la App
        self.pack(expand=True, fill="both")

        #Grid Layout
        self.rowconfigure((0,2), weight=1, uniform="a")
        self.rowconfigure((1), weight=7, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")

        #Widgets
        self.crear_widgets()
        self.posicion_widgets()
        self.agregar_eventos()

    #Creación de widgets
    def crear_widgets(self):
        #Frame desplegable
        self.frame_desplegable = CTkScrollableFrame(self)

        #Botones
        self.boton_volver = CTkButton(self, 
                                      text="volver", 
                                      command=self.controlador.volver)
        
        #Etiquetas
        self.titulo_eventos = CTkLabel(self, 
                                       text="Eventos", 
                                       font=("arial", 30, "bold"))

    #Posición de widgets
    def posicion_widgets(self):
        self.frame_desplegable.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        self.boton_volver.grid(row=2, column=0, padx=2, pady=2)
        self.titulo_eventos.grid(row=0, column=0, padx=2, pady=2)

    #Crea un frame ubicado dentro del frame desplegable con la info 
    #de un evento
    def crear_vista_para_evento(self, nombre_evento, hora_inicio, imagen):

        #Frame en el que se mostrará el evento
        frame_evento = CTkFrame(self.frame_desplegable,
                                fg_color="black")
        
        #Posición que tomará en el frame desplegable
        frame_evento.pack(expand=True, fill="both", padx=2, pady=2)

        #Grid Layout del frame
        frame_evento.rowconfigure((0,1), weight=1, uniform="a")
        frame_evento.columnconfigure((0,2), weight=1, uniform="a")
        frame_evento.columnconfigure((1), weight=2, uniform="a")

        #Widgets
        nombre_evento = CTkLabel(frame_evento, text=nombre_evento)
        foto_evento = CTkLabel(frame_evento, image=self.controlador.imagenes[imagen])
        etiqueta = CTkLabel(frame_evento, text=f"Fecha:")
        horario_etiqueta = CTkLabel(frame_evento, text=hora_inicio)

        #Posición
        nombre_evento.grid(row=0, column=1)
        foto_evento.grid(row=0, column=0, rowspan=2)
        etiqueta.grid(row=0, column=2)
        horario_etiqueta.grid(row=1, column=2)

    #crea un frame para cada evento
    def agregar_eventos(self):
        eventos = self.controlador.obtener_eventos()
        for evento in eventos:
            print(evento)
            #Se le resta 1 al id y se lo usa como indice para
            #mostrar la imagen en ese indice de la lista
            self.crear_vista_para_evento(evento.nombre, evento.hora_inicio, evento.id-1)
            