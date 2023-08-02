from customtkinter import *
from models.usuario import Usuario

class Controlador_login:
    def __init__(self, app):
        self.app = app


    #Crea un objeto de la clase Usuario y se lo añade a la lista de usuarios
    def iniciar_sesion(self, nombre, apellido):
        nuevo_usuario = {"id": self.app.usuarios[-1].id+1, "nombre":nombre, "apellido":apellido, "historial_eventos":[]}
        nuevo_usuario = Usuario.añadir_usuario(nuevo_usuario)

        print(f"usuarios registrados: {len(self.app.usuarios)}")
        self.app.usuarios.append(nuevo_usuario)
        print(f"usuarios registrados: {len(self.app.usuarios)}")
        print(f"Bienvenido: {nuevo_usuario.nombre} {nuevo_usuario.apellido}")
        self.app.vista_login.destroy()
        self.app.mostrar_inicio()