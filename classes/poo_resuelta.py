class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.stock}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado al inventario.")

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                print("Producto encontrado:")
                print(producto)
                return
        print(f"No se encontró un producto con el nombre '{nombre}'.")


# Ejemplo de uso:
if __name__ == "__main__":
    p1 = Producto("Laptop", 1200.00, 10)
    p2 = Producto("Mouse", 25.99, 50)

    inventario = Inventario()
    inventario.agregar_producto(p1)
    inventario.agregar_producto(p2)

    print("\nTodos los productos:")
    inventario.mostrar_productos()

    print("\nBuscando 'Mouse':")
    inventario.buscar_producto("Mouse")

    print("\nBuscando 'Teclado':")
    inventario.buscar_producto("Teclado")
