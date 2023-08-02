from customtkinter import *

class Vista_Usuario(CTkToplevel):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.controlador = controlador

        self.geometry("600x400+400+100")
        self.focus()


        self.frame = CTkFrame(self)
        self.frame.pack(expand=True, fill="both")

        #Grid Layout
        self.frame.rowconfigure((0,1,2,3), weight=1, uniform="a")
        self.frame.rowconfigure((4), weight=3, uniform="a")
        self.frame.columnconfigure((0,1,2,3), weight=1, uniform="a")

        #Widgets
        self.crear_widgets()
        self.posicion_widgets()
    

    def crear_widgets(self):
        #Etiquetas
        self.usuario_etiqueta = CTkLabel(self.frame, text="Detalles de Usuario", font=("Roboto", 30, "bold"))
        self.nombre_etiqueta = CTkLabel(self.frame, text=f"Nombre: {self.controlador.usuario.nombre}", font=("Roboto",20))
        self.apellido_etiqueta = CTkLabel(self.frame, text=f"Apellido: {self.controlador.usuario.apellido}", font=("Roboto",20))
        self.eventos_asistidos_etiqueta = CTkLabel(self.frame, text="Eventos asistidos:", font=("Roboto",20))

        #Botones
        self.boton_añadir = CTkButton(self.frame, width=100, text="Añadir", font=("Open Sans",15))
        self.boton_cerrar = CTkButton(self.frame, width=100, text="Cerrar", font=("Open Sans",15), command=self.controlador.cerrar)

    def posicion_widgets(self):
        self.usuario_etiqueta.grid(row=0, column=1, sticky="w", columnspan=4)
        self.nombre_etiqueta.grid(row=1, column=1, columnspan=2, sticky="w", padx=10, pady=5)
        self.apellido_etiqueta.grid(row=2, column=1, columnspan=2, sticky="w", padx=10, pady=5)
        self.eventos_asistidos_etiqueta.grid(row=3, column=1, columnspan=2, sticky="w", padx=10, pady=5)
        self.boton_añadir.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.boton_cerrar.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        