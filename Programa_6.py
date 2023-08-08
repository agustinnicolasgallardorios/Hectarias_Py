print("Bienvenido al calculador de hectarias")

calculador = float(input("ingrese aca el valor que desea convertir a hectarias "))

class terreno():

    def __init__ (self, calc, superficie):
        self.calc = calc
        self.sup = superficie

    def valor (self):
        print("La superficie final, es", self.calc * self.sup, "m2")

calculo_final = terreno(calculador, 100)
calculo_final.valor()

calculador = float(input("Gracias por usar el programa :)"))

    
    


