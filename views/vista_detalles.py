from customtkinter import *

class Vista_Detalle(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init()
        self.parent = parent
        self.controlador = controlador

        #Posición en la App
        self.pack(expand=True, fill="both")
