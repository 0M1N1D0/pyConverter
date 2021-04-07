# Docstring
"""Este modulo contendrá la implementación de la GUI"""

#importación de los paquetes
from tkinter import *
from clase_Menu import MenuPrincipal


# creación de la raíz y ventana principal 
raiz = Tk()
raiz.title('pyConverter')
raiz.geometry("300x0")
raiz.resizable(0,0)





objMenuPrincipal = MenuPrincipal(raiz)
raiz.mainloop()


