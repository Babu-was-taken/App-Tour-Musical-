from customtkinter import *

#Cambio de los colores de la interfaz visual
boton= "#E6D884"
borde= "#A1A892"
frame= "#E5E5E5"
titulo= "#2F242C"
texto= "#E6D884"



class Vista_Detalles(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color=frame)
        self.parent = parent
        self.controlador = controlador

        #Posición que tendrá en la App
        self.pack(expand=True, fil="both", padx=2, pady=2)

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
        #Frame desplegable en el que se mostrarán los detalles del evento
        self.detalles_frame = CTkScrollableFrame(self)
        self.interior_frame = CTkFrame(self.detalles_frame, height=300, fg_color=borde)


        #Grid Layout
        self.interior_frame.rowconfigure((0,1,2,3,4,5,6), weight=1, uniform="a")
        self.interior_frame.columnconfigure((0,1,2,3,4), weight=1, uniform="a")

        #Botones
        self.boton_volver = CTkButton(self, text="Volver",
                                      fg_color= boton,
                                      hover_color= borde,
                                      text_color= titulo,
                                      font=("Open Sans",20),
                                      command=self.controlador.volver)
        self.boton_detalles = CTkButton(self, text="Detalles", 
                                        fg_color= boton,
                                        hover_color= borde,
                                        text_color= titulo,
                                        font=("Open Sans",20),
                                        state="disabled")
        self.boton_ubicacion = CTkButton(self, text="Ubicación",
                                         fg_color=boton,
                                         text_color=titulo,
                                         hover_color=borde,
                                         font=("Open Sans",20),
                                         command=self.controlador.mostrar_seccion_ubicacion)
        
        #Etiquetas
        self.detalles_etiqueta = CTkLabel(self, text="Detalles", 
                                          text_color=titulo,
                                          font=("Roboto", 30, "bold"))
        self.nombre_etiqueta = CTkLabel(self.interior_frame, 
                                        text=self.controlador.evento_seleccionado.nombre, 
                                        text_color= texto,
                                        font=("Roboto", 15))
        self.artista = CTkLabel(self.interior_frame, 
                                text=f"Artista: {self.controlador.evento_seleccionado.artista}",
                                text_color= texto,
                                font=("Roboto",15))
        self.imagen = CTkLabel(self.interior_frame, image=self.parent.imagenes[self.controlador.evento_seleccionado.id-1])
        self.fecha_inicio = CTkLabel(self.interior_frame, 
                                     text=f"Desde: {self.controlador.evento_seleccionado.hora_inicio}",
                                     text_color=texto,
                                     font=("Roboto",15))
        self.fecha_fin = CTkLabel(self.interior_frame, 
                                  text=f"Hasta: {self.controlador.evento_seleccionado.hora_fin}",
                                  text_color= texto,
                                  font=("Roboto",15))
        self.descripbion_titulo = CTkLabel(self.interior_frame, text="Descripción", 
                                           text_color= texto,
                                           font=("Roboto", 20))
        self.descripcion = CTkLabel(self.interior_frame, 
                                    text=self.controlador.evento_seleccionado.descripcion,
                                    text_color= texto,
                                    font=("Open Sans",15))
        self.genero_titulo = CTkLabel(self.interior_frame, 
                                      text="Género",
                                       text_color= texto,
                                         font=("Roboto", 20))
        self.genero = CTkLabel(self.interior_frame, 
                               text=self.controlador.evento_seleccionado.genero,
                               text_color=texto,
                               font=("Open Sans",13),)


    #Posición de widgets
    def posicion_widgets(self):
        self.detalles_frame.grid(row=1, column=1, rowspan=7, padx=5, pady=5, sticky="nsew")
        self.interior_frame.pack(expand=True, fill="x", padx=2, pady=2)

        self.boton_volver.grid(row=1, column=0, padx=5, pady=5)
        self.boton_detalles.grid(row=2, column=0, padx=5, pady=5)
        self.boton_ubicacion.grid(row=3, column=0, padx=5, pady=5)
        self.detalles_etiqueta.grid(row=0, column=1, padx=5, pady=5)
        self.nombre_etiqueta.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        self.artista.grid(row=1, column=2, columnspan=2, sticky="w", padx=5, pady=5)
        self.imagen.grid(row=1, column=0, rowspan=2, columnspan=2, sticky="w", padx=10, pady=5)
        self.fecha_inicio.grid(row=2, column=2, columnspan=2, sticky="nw", padx=5, pady=5)
        self.fecha_fin.grid(row=2, column=2, columnspan=2, sticky="sw", padx=5, pady=5)
        self.descripbion_titulo.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        self.descripcion.grid(row=4, column=0, columnspan=5, sticky="w", padx=10, pady=5)
        self.genero_titulo.grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        self.genero.grid(row=6, column=0, columnspan=5, sticky="w", padx=10, pady=5)