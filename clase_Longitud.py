from tkinter import *

class VentanaLongitud:
    """Contiene toda la implementación de la ventana Longitud"""
    def __init__(self):
        
        # creación de la ventana 
        #self.miframe = Frame()
        # self.miframe.pack()
        
        self.ventana_longitud = Toplevel()
        self.ventana_longitud.geometry("350x100")
        self.ventana_longitud.title("Conversiones de longitud")

        
        # indica que el menu se insertará en la ventana longitud
        self.menubar = Menu(self.ventana_longitud)
        self.ventana_longitud.config(menu=self.menubar)


        # menu principal Archivo
        self.archivo_menu = Menu(self.menubar, tearoff=0)
        # sud menu de Archivo
        self.archivo_menu.add_command(label="Nuevo")
        self.archivo_menu.add_command(label="Salir", command=self.ventana_longitud.destroy)


        self.menubar.add_cascade(label='Archivo', menu=self.archivo_menu)

        