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
print("Ejercicio 1 y 2: Crear una clase Persona")

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
class Product:
    def __init__(self,nombre, precio ,stock)-> None :
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
            print(f"producto vendido queda {cantidad -1} unidad")
ventas = Product("tv",9000,2)
ventas1=Product("tablet",1000,1)
ventas3=Product("radio",1000,1)
ventas.vender()
ventas1.vender()
ventas3.vender()
"""Ejercicios de Programacion Orientada a Objetos en Python
Ejercicio 1: Crear una clase Persona
Objetivo: Crear una clase simple con atributos y mostrar su uso.
Instrucciones:
1. Crear una clase llamada `Persona`.
2. Esta clase debe tener los atributos `nombre` y `edad`.
3. El constructor (`__init__`) debe recibir esos dos datos como parámetros.
4. Crear una instancia de `Persona` con tus propios datos.
5. Imprimir en pantalla el nombre y edad de la persona.
Requisitos: uso de `__init__`, atributos de instancia, impresión con `print()`.
Ejercicio 2: Agregar un método a la clase
Objetivo: Añadir un comportamiento a la clase con un método.
Instrucciones:
1. A partir del ejercicio anterior, agregar un método llamado `presentarse` a la clase `Persona`.
2. Este método debe imprimir: "Hola, me llamo <nombre> y tengo <edad> años."
3. Llamar al método `presentarse()` desde el objeto creado.
Requisitos: definir un método, uso de `self`, f-strings.
Ejercicio 3: Crear una clase Producto
Objetivo: Práctica con clases, atributos y lógica básica.
Instrucciones:
1. Crear una clase `Producto` con los atributos: `nombre`, `precio` y `stock`.
2. Crear un método llamado `mostrar_info` que imprima los datos del producto.
3. Crear otro método llamado `vender` que reste 1 unidad al stock y muestre un mensaje del tipo: "Producto vendido.
Quedan X unidades."
4. Si el stock es 0, debe imprimir: "No hay más stock disponible."
Requisitos: condicionales, métodos que modifican atributos.
Ejercicio 4: Herencia básica - clase Estudiante
Objetivo: Crear una subclase que herede de otra.
Instrucciones:
1. Partiendo de la clase `Persona`, crear una nueva clase llamada `Estudiante` que herede de `Persona`.
2. El estudiante debe tener un atributo adicional: `carrera`.
3. Crear un método llamado `datos_estudiante` que imprima: "Soy <nombre>, tengo <edad> años y estudio <carrera>."
4. Crear un objeto de la clase `Estudiante` y mostrar sus datos con el nuevo método.
Requisitos: herencia, nuevos atributos, métodos.
Ejercicio 5: Usar `super()` en la subclase
Objetivo: Utilizar `super()` para inicializar atributos del padre.
Instrucciones:

Ejercicios de Programacion Orientada a Objetos en Python
1. Modificar el constructor de la clase `Estudiante` para que use `super().__init__(...)`.
2. Verificar que los atributos `nombre` y `edad` se asignan correctamente usando `super()`.
Requisitos: uso correcto de `super()`.
Ejercicio 6: Clase Vehiculo y subclases
Objetivo: Aplicar herencia para crear distintos tipos de objetos.
Instrucciones:
1. Crear una clase base `Vehiculo` con los atributos: `marca` y `modelo`.
2. Agregar un método `arrancar()` que imprima "El vehículo está en marcha".
3. Crear dos clases que hereden de `Vehiculo`: `Auto` y `Moto`.
4. En la clase `Auto`, crear un método `tocar_bocina()` que imprima "Beep beep!".
5. En la clase `Moto`, crear un método `hacer_wheelie()` que imprima "¡Haciendo wheelie!".
6. Crear un objeto de cada clase y llamar a sus métodos.
Requisitos: herencia, métodos específicos.
Ejercicio 7: Polimorfismo simple
Objetivo: Entender cómo distintas clases pueden tener métodos con el mismo nombre pero distinto comportamiento.
Instrucciones:
1. En `Auto` y `Moto`, agregar un método `tipo_vehiculo()` que:
- En `Auto` imprima "Soy un auto".
- En `Moto` imprima "Soy una moto".
2. Crear una lista con objetos `Auto` y `Moto`.
3. Usar un `for` para recorrer la lista y llamar a `tipo_vehiculo()` en cada uno.
Requisitos: polimorfismo, listas, bucles.
Ejercicio 8: Bonus - Inventario de productos (integrador)
Objetivo: Integrar varios conceptos.
Instrucciones:
1. Crear una clase `Producto` con nombre, precio y stock.
2. Crear una clase `Inventario` que mantenga una lista de productos.
3. El método `agregar_producto` debe recibir un producto y agregarlo a la lista.
4. El método `mostrar_productos` debe imprimir todos los productos del inventario.
5. El método `buscar_producto(nombre)` debe buscar un producto por nombre e imprimirlo si existe.
Requisitos: listas de objetos, clases que contienen otras, métodos con parámetros."""
class Producto():
    def __init__(self,nombre, precio, stock) -> None:
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
class Inventario():
    def __init__(self) :
        self.productos = []

    def agregar_producto(self,producto):
        self.productos.append(producto)
        for product in self.productos:
            print(product)
    

        return f"estos son los {self.productos} que existen"
    def busqueda(self):
        pass
   
        

        
 