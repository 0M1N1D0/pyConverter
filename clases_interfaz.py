from tkinter import *

class MenuPrincipal:
    """Clase para el menu principal de la ventana"""
    
    def __init__(self, master):
        # docstring
        '''Crea el menu principal junto con sus submenus'''
        miFrame = Frame(master)
        miFrame.pack()
    
 
        # creación del menú 
        menubar = Menu(master)
        master.config(menu=menubar)


        # menu principal
        self.archivo_menu = Menu(menubar, tearoff=0)
        # submenus
        self.archivo_menu.add_command(label="Nuevo")
        self.archivo_menu.add_command(label="Salir", command=master.quit)
        # menu principal
        self.conversiones_menu = Menu(menubar, tearoff=0)
        # submenus
        self.conversiones_menu.add_command(label="Longitud")
        self.conversiones_menu.add_command(label="Volumen")
        self.conversiones_menu.add_command(label="Peso y masa")
        self.conversiones_menu.add_command(label="Temperatura")
        self.conversiones_menu.add_command(label="Energía")
        self.conversiones_menu.add_command(label="Área")
        self.conversiones_menu.add_command(label="Velocidad")
        self.conversiones_menu.add_command(label="Tiempo")
        self.conversiones_menu.add_command(label="Potencia")
        self.conversiones_menu.add_command(label="Moneda")
        # menu principal
        self.ayuda_menu = Menu(menubar, tearoff=0)


        menubar.add_cascade(label='Archivo', menu=self.archivo_menu)
        menubar.add_cascade(label='Conversiones', menu=self.conversiones_menu)
        menubar.add_cascade(label='Ayuda', menu=self.ayuda_menu)
