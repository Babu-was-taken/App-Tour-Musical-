from customtkinter import *
from tkintermapview import TkinterMapView

#Cambio de los colores de la interfaz visual
boton= "#E6D884"
borde= "#A1A892"
frame= "#E5E5E5"
titulo= "#2F242C"
texto= "#E6D884"

class Vista_Mapa(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color= frame,border_color= borde)

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

        self.agregar_marcador()

    def crear_widgets(self):
        #Frame que mostrará la ubicación del evento en el mapa
        self.mapa_frame = CTkFrame(self, fg_color="")

        #Mapa
        self.mapa = TkinterMapView(self.mapa_frame, corner_radius=0)

        #Botones
        self.boton_volver = CTkButton(self, text="Volver", command=self.controlador.volver,fg_color= boton,font=("Open Sans",15),text_color= titulo,border_color= borde)
        self.boton_detalles = CTkButton(self, text="Detalles", command=self.controlador.mostrar_seccion_detalles,fg_color= boton,font=("Open Sans",15),text_color= titulo,border_color= borde)
        self.boton_ubicacion = CTkButton(self, text="Ubicación", state="disabled",fg_color= boton,font=("Open Sans",15),text_color= titulo,border_color= borde)

        #Etiquetas
        self.ubicacion_etiqueta = CTkLabel(self, text="Ubicación en el mapa", text_color= titulo , font=("Roboto", 30, "bold"))



    def posicion_widgets(self):
        self.mapa_frame.grid(row=1, column=1, rowspan=5, sticky="nsew", padx=5, pady=5)
        
        self.mapa.pack(expand=True, fill="both")

        self.ubicacion_etiqueta.grid(row=0, column=1)

        self.boton_volver.grid(row=1, column=0, padx=5, pady=5)
        self.boton_detalles.grid(row=2, column=0, padx=5, pady=5)
        self.boton_ubicacion.grid(row=3, column=0, padx=5, pady=5)


    #Coloca un marcador en la ubicación del evento seleccionado
    def agregar_marcador(self):
        ubicacion_seleccionada = self.controlador.ubicacion_seleccionada
        self.mapa.set_position(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)
        self.mapa.set_marker(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)
        print(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)