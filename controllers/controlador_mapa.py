from customtkinter import *
class Controlador_Mapa:
    def __init__(self, app, ubicacion_seleccionada):
        self.app = app
        self.ubicacion_seleccionada = ubicacion_seleccionada

    def cargar_marcadores(self, mapa):
        imagen = self.app.imagenes[self.ubicacion_seleccionada.id-1]
        marcador = mapa.agregar_marcador(self.ubicacion_seleccionada, imagen)
        marcador.hide_image(True)

    #Al clickear el marcador genera la imagen del evento seleccionado
    def seleccionar_ubicacion(self,marcador):
        if marcador.image_hidden is True:
            marcador.hide_image(False)
            print("Ubicación seleccionada: ", marcador.text)
        else:
            marcador.hide_image(True)


    def mostrar_seccion_detalles(self):
        self.app.vista_mapa.destroy()
        self.app.mostrar_detalles()
        self.app.mostrar_comentarios()

    def volver(self):
        self.app.vista_mapa.destroy()

        self.app.mostrar_explorar()
        self.app.mostrar_eventos()