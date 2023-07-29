from customtkinter import *
from tkintermapview import TkinterMapView

class Vista_Mapa(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color="black")
        self.controlador = controlador

        #Posición en la vista Detalles
        self.grid(row=1, column=0, sticky="nsew")

        #Mapa
        self.mapa = TkinterMapView(self, corner_radius=0)
        self.mapa.set_position(-34.613072565438195, -58.37043644907444)
        self.mapa.pack(expand=True, fill="both")