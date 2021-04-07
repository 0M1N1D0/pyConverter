from tkinter import *
from clase_Longitud import VentanaLongitud

class MenuPrincipal:
    """Clase para el menu principal de la ventana"""
    
    def __init__(self, master):
        self.master = master
        # docstring
        '''Crea el menu principal junto con sus submenus'''
        self.miFrame = Frame(self.master)
        self.miFrame.pack()
    
 
        # creación del menú 
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)


        # menu principal
        self.archivo_menu = Menu(self.menubar, tearoff=0)
        # submenus
        self.archivo_menu.add_command(label="Nuevo")
        self.archivo_menu.add_command(label="Salir", command=self.master.quit)
        # menu principal
        self.conversiones_menu = Menu(self.menubar, tearoff=0)
        # submenus
        self.conversiones_menu.add_command(label="Longitud", command=VentanaLongitud)
        self.conversiones_menu.add_command(label="Volumen")
        self.conversiones_menu.add_command(label="Peso y masa")
        self.conversiones_menu.add_command(label="Temperatura")
        self.conversiones_menu.add_command(label="Energía")
        self.conversiones_menu.add_command(label="Área")
        self.conversiones_menu.add_command(label="Velocidad")
        self.conversiones_menu.add_command(label="Tiempo")
        self.conversiones_menu.add_command(label="Potencia")
        self.conversiones_menu.add_command(label="Datos")
        self.conversiones_menu.add_command(label="Presión")
        self.conversiones_menu.add_command(label="Ángulo")
        self.conversiones_menu.add_command(label="Moneda")
        # menu principal
        self.ayuda_menu = Menu(self.menubar, tearoff=0)


        self.menubar.add_cascade(label='Archivo', menu=self.archivo_menu)
        self.menubar.add_cascade(label='Conversiones', menu=self.conversiones_menu)
        self.menubar.add_cascade(label='Ayuda', menu=self.ayuda_menu)
