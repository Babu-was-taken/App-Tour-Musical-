from customtkinter import *

class Vista_Detalles(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color="black")
        self.parent = parent
        self.controlador = controlador

        #Posición que tendrá en la App
        self.pack(expand=True, fill="both")

        #Grid Layout
        self.rowconfigure((0,1,3,4,5,6), weight=1, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")
        self.columnconfigure(1, weight=5, uniform="a")

        #Widgets
        self.crear_widgets()
        self.posicion_widgets()

    #Creación de widgets
    def crear_widgets(self):
        #Frames
        #Frame en el que se mostrarán los detalles del evento
        self.detalles_frame = CTkFrame(self, fg_color="black")
        #Frame que mostrará la ubicación del evento en el mapa
        self.ubicacion_frame = CTkFrame(self, fg_color="black")
        self.ubicacion_frame.rowconfigure((0), weight=1, uniform="a")
        self.ubicacion_frame.rowconfigure((1), weight=10, uniform="a")
        self.ubicacion_frame.columnconfigure((0), weight=1, uniform="a")


        #Botones
        self.boton_volver = CTkButton(self, text="Volver",
                                      command=self.controlador.volver)
        self.boton_detalles = CTkButton(self, text="detalles",
                                        command=self.controlador.mostrar_seccion_detalles)
        self.boton_ubicacion = CTkButton(self, text="Ubicación",
                                         command=self.controlador.mostrar_seccion_ubicacion)
        
        #Etiquetas
        self.detalles_etiqueta = CTkLabel(self.detalles_frame, text="Detalles")
        self.ubicacion_etiqueta = CTkLabel(self.ubicacion_frame, text="Ubicación en el mapa")


    #Posición de widgets
    def posicion_widgets(self):
        self.detalles_frame.grid(row=0, column=1, rowspan=5, padx=5, pady=5, sticky="nsew")
        self.ubicacion_frame.grid(row=0, column=1, rowspan=5, padx=5, pady=5, sticky="nsew")


        self.boton_volver.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
        self.boton_detalles.grid(row=1, column=0, padx=5, pady=5, sticky="nw")
        self.boton_ubicacion.grid(row=2, column=0, padx=5, pady=5, sticky="nw")
        self.detalles_etiqueta.grid(row=0, column=0)
        self.ubicacion_etiqueta.grid(row=0, column=0)




