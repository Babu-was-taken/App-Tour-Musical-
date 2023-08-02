from customtkinter import *
import webbrowser
import urllib.parse
from models.review import Review

class Controlador_Detalles:
    def __init__(self, app, evento_seleccionado):
        self.app = app
        self.evento_seleccionado = evento_seleccionado

    def mostrar_seccion_ubicacion(self):
        self.app.vista_detalles.destroy()
        self.app.mostrar_ubicacion()

    def volver(self):
        self.app.vista_detalles.destroy()
        self.app.mostrar_explorar()
        self.app.mostrar_eventos()

    def ver_perfil(self, id):
        self.app.seleccionar_usuario(id)
        self.app.mostrar_usuario()

    def compartir(self):
        message = "Hey, échale un vistazo a este evento! :)"
        url= "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
        message = urllib.parse.quote(message)
        url = urllib.parse.quote(url)
        share_url = f"https://twitter.com/intent/tweet?text={message}&url={url}"
        webbrowser.open_new_tab(share_url)


    #Crea un objeto de la clase Review y lo agrega a la lista de comentarios
    def enviar_comentario(self, nota, animo, comentario):
        nuevo_comentario = {"id": self.app.comentarios[0].id-1, 
                            "id_evento":self.evento_seleccionado.id, 
                            "id_usuario":self.app.usuarios[-1].id, 
                            "calificacion":nota, 
                            "comentario":comentario,
                            "animo":animo}
        nuevo_comentario = Review.añadir_comentario(nuevo_comentario)

        print(f"{len(self.app.comentarios)} comentarios registrados")
        self.app.comentarios.insert(0, nuevo_comentario)                #Se lo inserta a la posición 0 para que aparezca al principio cuando se actualize la vista
        print(f"{len(self.app.comentarios)} comentarios registrados")
        print(f"comentario añadido: {nuevo_comentario.calificacion, nuevo_comentario.animo, nuevo_comentario.comentario}")

        self.app.vista_comentarios.destroy()
        self.app.mostrar_comentarios()