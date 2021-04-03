# Docstring
"""Este modulo contendrá la implementación de la GUI"""

#importación de los paquetes
from tkinter import *


# creando la ventana
raiz = Tk()
raiz.title('pyConverter')
raiz.geometry('500x500')
raiz.resizable(1,1)


# creación del menú 
menubar = Menu(raiz)
raiz.config(menu=menubar)


# menu principal
archivo_menu = Menu(menubar, tearoff=0)
# submenus
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Salir", command=raiz.quit)
# menu principal
conversiones_menu = Menu(menubar, tearoff=0)
# submenus
conversiones_menu.add_command(label="Volumen")
conversiones_menu.add_command(label="Longitud")
conversiones_menu.add_command(label="Peso y masa")
conversiones_menu.add_command(label="Temperatura")
conversiones_menu.add_command(label="Energía")
conversiones_menu.add_command(label="Área")
conversiones_menu.add_command(label="Velocidad")
conversiones_menu.add_command(label="Tiempo")
conversiones_menu.add_command(label="Potencia")
conversiones_menu.add_command(label="Moneda")
# menu principal
ayuda_menu = Menu(menubar, tearoff=0)


menubar.add_cascade(label='Archivo', menu=archivo_menu)
menubar.add_cascade(label='Conversiones', menu=conversiones_menu)
menubar.add_cascade(label='Ayuda', menu=ayuda_menu)



# creando el frame
frame = Frame(raiz)
frame.grid(row=0, column=0)


raiz.mainloop()



