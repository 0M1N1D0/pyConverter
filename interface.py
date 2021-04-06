# Docstring
"""Este modulo contendrá la implementación de la GUI"""

#importación de los paquetes
from tkinter import *
from clase_Menu import MenuPrincipal


# creación de la raíz y ventana principal 
raiz = Tk()
raiz.title('pyConverter')
raiz.geometry("300x300")
raiz.resizable(1,1)





objMenuPrincipal = MenuPrincipal(raiz)
raiz.mainloop()


