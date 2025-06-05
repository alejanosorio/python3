"""Ejercicios de Programacion Orientada a Objetos en Python
Ejercicio 1: Crear una clase Persona
Objetivo: Crear una clase simple con atributos y mostrar su uso.
Instrucciones:
1. Crear una clase llamada `Persona`.
2. Esta clase debe tener los atributos `nombre` y `edad`.
3. El constructor (`__init__`) debe recibir esos dos datos como parámetros.
4. Crear una instancia de `Persona` con tus propios datos.
5. Imprimir en pantalla el nombre y edad de la persona.
Requisitos: uso de `__init__`, atributos de instancia, impresión con `print()"""
print("Ejercicio 1: Crear una clase Persona")

class Persona:
    def __init__(self,nombre,edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    def presentacion(self):
        print(f"hola me llamo {self.nombre} y tengo {self.edad} ")
        
        
datos = Persona("ALEX",47)
Persona.presentacion(datos)
"""
1. Crear una clase `Producto` con los atributos: `nombre`, `precio` y `stock`.
2. Crear un método llamado `mostrar_info` que imprima los datos del producto.
3. Crear otro método llamado `vender` que reste 1 unidad al stock y muestre un mensaje del tipo: "Producto vendido.
Quedan X unidades."
4. Si el stock es 0, debe imprimir: "No hay más stock disponible."
Requisitos: condicionales, métodos que modifican atributos."""
print("Ejercicio 3: Crear una clase Producto")
class Producto:
    def __init__(self,nombre, precio ,stock) :
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def mostrar_info(self):
        print(f" el producto se llama {self.nombre} y vale {self.precio} y en stock esta en  {self.stock}")
        
       
    def vender(self):
        cantidad = self.stock 
        if cantidad == 0:
             print("No hay más stock disponible.")
           
        else:
            print(f"producto vendido quedan {cantidad -1}")
           
       
      
               
            
ventas = Producto("tv",9000,8)
print(ventas.vender())