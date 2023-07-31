from customtkinter import *
class Vista_Detalles(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color="black")
        self.parent = parent
        self.controlador = controlador

        #Posición que tendrá en la App
        self.pack(expand=True, fil="both")

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

        #Grid Layout
        self.detalles_frame.rowconfigure((0), weight=1, uniform="a")
        self.detalles_frame.rowconfigure((1,2,3,4,5), weight=2, uniform="a")
        self.detalles_frame.rowconfigure((6), weight=5, uniform="a")
        self.detalles_frame.columnconfigure((0,1,2), weight=1, uniform="a")


        #Botones
        self.boton_volver = CTkButton(self, text="Volver",
                                      command=self.controlador.volver)
        self.boton_detalles = CTkButton(self, text="detalles", state="disabled")
        self.boton_ubicacion = CTkButton(self, text="Ubicación",
                                         command=self.controlador.mostrar_seccion_ubicacion)

        #Etiquetas
        self.detalles_etiqueta = CTkLabel(self.detalles_frame, text="Detalles", font=("arial", 30, "bold"))
        self.nombre_etiqueta = CTkLabel(self.detalles_frame, text=self.controlador.evento_seleccionado.nombre, font=("arial", 20))
        self.artista = CTkLabel(self.detalles_frame, text=f"Artista: {self.controlador.evento_seleccionado.artista}")
        #self.imagen = CTkLabel(self.detalles_frame, image=self.parent.imagenes[self.controlador.evento_seleccionado.id-1])
        self.fecha_inicio = CTkLabel(self.detalles_frame, text=f"Desde: {self.controlador.evento_seleccionado.hora_inicio}")
        self.fecha_fin = CTkLabel(self.detalles_frame, text=f"Hasta: {self.controlador.evento_seleccionado.hora_fin}")
        self.genero = CTkLabel(self.detalles_frame, text=f"Genero: {self.controlador.evento_seleccionado.genero}")
        self.descripcion = CTkLabel(self.detalles_frame, text=self.controlador.evento_seleccionado.descripcion)



    #Posición de widgets
    def posicion_widgets(self):
        self.detalles_frame.grid(row=0, column=1, rowspan=7, padx=5, pady=5, sticky="nsew")

        self.boton_volver.grid(row=1, column=0, padx=5, pady=5)
        self.boton_detalles.grid(row=2, column=0, padx=5, pady=5)
        self.boton_ubicacion.grid(row=3, column=0, padx=5, pady=5)

        self.detalles_etiqueta.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.nombre_etiqueta.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        self.artista.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        #self.imagen.grid(row=1, column=0, rowspan=2, columnspan=2, sticky="nsew")
        self.fecha_inicio.grid(row=1, column=2, padx=5, pady=5)
        self.fecha_fin.grid(row=2, column=2, padx=5, pady=5)
        self.genero.grid(row=3, column=0, columnspan=3, sticky="w", padx=10, pady=5)
        self.descripcion.grid(row=4, column=0, columnspan=3, sticky="w", padx=10, pady=5)