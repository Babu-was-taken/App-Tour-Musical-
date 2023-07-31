from customtkinter import *
from PIL import Image, ImageTk
from models.evento import Evento
from views.vista_inicio import Vista_Inicio
from views.vista_explorar import Vista_Explorar
from views.vista_eventos import Vista_Eventos
from views.vista_detalles import Vista_Detalles
from views.vista_comentarios import Vista_Comentarios
from views.vista_mapa import Vista_Mapa
from controllers.controlador_inicio import Controlador_Inicio
from controllers.controlador_explorar import Controlador_Explorar
from controllers.controlador_eventos import Controlador_Eventos
from controllers.controlador_detalles import Controlador_Detalles
from controllers.controlador_mapa import Controlador_Mapa
from models.Ubicacion import Ubicacion
from models.review import Review
from models.usuario import Usuario

set_default_color_theme("dark-blue")

class App(CTk):
    def __init__(self, imagenes=[]):
        super().__init__()
        #Setup principal
        self.title("App Tour Musical 0.1")
        self.geometry("700x500")
        self.minsize(600,400)
        self.maxsize(800,600)


        #Se cargan los eventos y las ubicaciones
        self.eventos = Evento.cargar_de_json("data/evento.json")
        self.ubicaciones = Ubicacion.cargar_de_json("data/ubicacion.json")
        self.comentarios = Review.cargar_de_json("data/review.json")
        self.usuarios = Usuario.cargar_de_json("data/usuario.json")
        self.imagenes = imagenes
        print(self.ubicaciones)

        #Inicializar
        self.inicializar()
        self.cargar_imagenes()

        #Run 
        self.mainloop()

    def inicializar(self):
        #Se cargan los controladores y se les asigna la lista de eventos
        self.controlador_inicio = Controlador_Inicio(self)
        self.controlador_explorar = Controlador_Explorar(self)
        self.Controlador_eventos = Controlador_Eventos(self, self.eventos)
        self.controlador_detalles = Controlador_Detalles(self, None)
        self.controlador_mapa = Controlador_Mapa(self, None)


        #Se muestra la pantalla inicial
        self.mostrar_inicio()

    #Añade las imagenes a la lista
    def cargar_imagenes(self):
        for evento in self.eventos:
            imagen = ImageTk.PhotoImage(Image.open(f"assets/{evento.imagen}").resize((200, 200)))
            self.imagenes.append(imagen)


    #Mostrar vistas
    def mostrar_inicio(self):
        self.vista_inicio = Vista_Inicio(self, self.controlador_inicio)

    def mostrar_explorar(self):
        self.vista_explorar = Vista_Explorar(self, self.controlador_explorar)
        self.vista_eventos = Vista_Eventos(self.vista_explorar, self.Controlador_eventos)

    def mostrar_detalles(self):
        self.vista_detalles = Vista_Detalles(self, self.controlador_detalles)
        self.vista_comentarios = Vista_Comentarios(self.vista_detalles.detalles_frame, self.controlador_detalles)

    def mostrar_ubicacion(self):
        self.vista_mapa = Vista_Mapa(self, self.controlador_mapa)


    def seleccionar_evento(self, id):
        for ubicacion, evento in zip(self.ubicaciones, self.eventos):
            if ubicacion.id and evento.id == id:
               self.ubicacion_seleccionada = ubicacion
               self.evento_seleccionado = evento
               self.controlador_detalles = Controlador_Detalles(self, evento)
               self.controlador_mapa = Controlador_Mapa(self, ubicacion)
               
               print(f"ID del evento seleccionado {id}")
               print(self.eventos[id-1].nombre)




App()

