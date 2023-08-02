from customtkinter import *

class Vista_Usuario(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent)

        #Posición que tendrá en la app                                              
        self.pack(expand=True, fill="both")

        