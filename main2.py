from customtkinter import *
from tkintermapview import TkinterMapView
from models.Ubicacion import Ubicacion2
from models.evento import Evento
#from controller.controlador_principal import ControladorPrincipal

class App(CTk):
    def __init__(self):
        super().__init__()
        

        self.frame_mapa = CTkFrame(self, fg_color="red")
        self.frame_mapa.pack(expand=True, fill="both")

        self.mapa = TkinterMapView(self.frame_mapa, width=600, height=600, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.pack(expand=True, fill="both")


        self.ubicaciones = Ubicacion2.cargar_de_json("data/ubicacion2.json")
        print(self.ubicaciones)



        self.mainloop()




App()