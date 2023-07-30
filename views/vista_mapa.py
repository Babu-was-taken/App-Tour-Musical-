from customtkinter import *
from tkintermapview import TkinterMapView

class Vista_Mapa(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color="black")
        self.parent = parent
        self.controlador = controlador

        #Posición en la vista Detalles
        self.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

        #Mapa
        self.mapa = TkinterMapView(self, corner_radius=0)
        self.mapa.pack(expand=True, fill="both")

        self.agregar_marcador()


    #Coloca un marcador en la ubicación del evento seleccionado
    def agregar_marcador(self):
        ubicacion_seleccionada = self.controlador.ubicacion_seleccionada
        self.mapa.set_position(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)
        self.mapa.set_marker(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)
        print(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)