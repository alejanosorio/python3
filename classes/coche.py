class Vehiculo():
    def __init__(self,ruedas,marca,modelo,color) -> None:
        self.ruedas = ruedas
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def acelerar(self):
        return f"acelerando"
        
mi_auto = Vehiculo(4,"dogde",1978,"red")
print(f"mi auto es de la marca {mi_auto.marca} y esta {mi_auto.acelerar()}")

class Bicicleta(Vehiculo):
    pass

