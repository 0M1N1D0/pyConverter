"""Clase que contendrá todos los calores de las conversiones"""

class Longitud:
    
    def __init__(self, opcion1, opcion2, valor):
        self.opcion1 = opcion1
        self.opcion2 = opcion2
        self.valor = valor

        

    def de_nanometro_a_micrones(self):
        resul = self.valor * 0.001
        return resul

        


# demostración
op1 = "nanometros"
op2 = "micrones"

if op1 == "nanometros" and op2 == "micrones":
    ob = Longitud(op1, op2, 10)
    ob.de_nanometro_a_micrones()

print(ob.de_nanometro_a_micrones())
