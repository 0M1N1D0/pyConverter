import numpy as np # para dar formato decial a los numeros muy pequeños
"""Clase que contendrá todos los calores de las conversiones"""

class Longitud:
    
    # constructor de la clase
    def __init__(self, opcion1, opcion2, valor):
        self.opcion1 = opcion1
        self.opcion2 = opcion2
        self.valor = valor

        
    # ************** DE NANOMETRO A ... ***************************

    def de_nanometros_a_micrones(self):
        resul = self.valor * 0.001
        return resul

    def  de_nanometros_a_milimetros(self):
        """
        1 nanometros ---- 0.000001 milimetros
        12 nanometros ---- x       
        """
        resul = self.valor * 0.000001
        resul = np.format_float_positional(resul, trim='-')
        return resul


    def de_nanometros_a_centimetros(self):
        """
        1 nanometros ---- 0.0000001 milimetros
        12 nanometros ---- x       
        """
        resul = self.valor * 0.0000001
        resul = np.format_float_positional(resul, trim='-')
        return resul

# # demostración
# op1 = "nanometros"
# op2 = "micrones"

# if op1 == "nanometros" and op2 == "micrones":
#     ob = Longitud(op1, op2, 120)
#     ob.de_nanometro_a_micrones()

# print(ob.de_nanometro_a_micrones())

ob = Longitud("a","b",1) 
# print('{:.20f}'.format(ob.de_nanometros_a_centimetros())) esta forma sólo le da el formato con la presición especificada 
print(ob.de_nanometros_a_centimetros())
