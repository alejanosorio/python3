class Vehiculo():
    def __init__(self,ruedas,marca,modelo,color) -> None:
        self.ruedas = ruedas
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def acelerar(self):
        return f"acelerando"
        


class Bicicleta(Vehiculo):
    def __init__(self, ruedas, marca, modelo, color,luces) -> None:
        super().__init__(ruedas, marca, modelo, color)
        self.luces = luces
    def mostrar_bici(self):
        print (f"mi bici tiene {self.ruedas} ruedas, es de la marca {self.marca} {self.modelo} es de color {self.color} y esta vendida")
        
andar = Bicicleta(2,"bianchi",2012,"red",True)
Bicicleta.mostrar_bici(andar)

