"""1- Crea unalista con los números del 1 al 5. Muestra el contenido de la lista por pantalla.
2- Crea una lista vacía. Agrega los nombres "Ana", "Luis" y "Carlos" usando el método append() y luego imprime la lista.
3- Dada la lista frutas = ["manzana", "banana", "naranja"], cambia el segundo elemento por "pera" y muestra la lista modificada.
4- Crea una tupla con tres colores: "rojo", "verde", "azul". Muestra el segundo color.
5- Dada la tupla datos = (10, 20, 30), conviértela en una lista, agrega el número 40, y vuelve a convertirla en tupla.
6- Dada la tupla numeros = (1, 2, 2, 3, 4, 2), cuenta cuántas veces aparece el número 2.
7- Crea un conjunto a partir de la lista nombres = ["Ana", "Luis", "Ana", "Carlos"] y muestra el resultado.
8- Crea un conjunto con los números del 1 al 5. Pregunta si el número 3 está en el conjunto.
9- Dado A = {1, 2, 3} y B = {3, 4, 5}, muestra la intersección de ambos conjuntos.
10- Crea un diccionario con claves "nombre", "edad" y "ciudad", con tus propios datos. Muestra el valor de "ciudad".
11- Dado el diccionario alumno = {"nombre": "Lucía", "nota": 7}, cambia la nota a 9 y agrega la clave "aprobado" con el valor True.

12- Dado el diccionario colores = {"rojo": "red", "azul": "blue", "verde": "green"}, muestra todas las claves y valores uno por uno."""
print("------------------ejercicio 2  ---------------\n")
my_lista = [] # type: ignore
a = "Ana","Luis" ,"Carlos"
my_lista.append(a)
print(my_lista)

print("------------------ejercicio 3 ---------------\n")
frutas = ["manzana", "banana", "naranja"]
frutas[1] = "pera"
print(frutas)


print("------------------ejercicio 4 ---------------\n")
colores = ("rojo", "verde", "azul")
print(colores[1])
print("------------------ejercicio 5 ---------------\n")
datos = (10, 20, 30)

# Convertir a lista
lista_datos:list[int] = list(datos) 

# Agregar el número 40
lista_datos.append(40)
#print(lista_datos)
my_tuple = tuple(lista_datos)
print(my_tuple)

print("------------------ejercicio 6 ---------------\n")
numeros = (1, 2, 2, 3, 4, 2)
print(f"el numero aparece {numeros.count(2)} veces")
mi_conjunto = {1, 3, 2, 9, 3, 1}
mi = list(mi_conjunto)
print(type(mi))

print("------------------ejercicio 7 ---------------\n")
nombres = set (["Ana", "Luis", "Ana", "Carlos"])
print(nombres)

print("------------------ejercicio 8 ---------------\n")
conjunto ={1,2,3,4,5}
print(3 in conjunto)
print("------------------ejercicio 9 ---------------\n")
A = {1, 2, 3} 
B = {3, 4, 5}
print(A.intersection(B))
print("------------------ejercicio 10 ---------------\n")
datas = {"nombre":"alex","edad":53,"cuidad":"gral. pinedo"}
salida =datas["cuidad"]
print(salida)
print("------------------ejercicio 11 ---------------\n")
alumno = {"nombre": "Lucía", "nota": 7}
alumno["nota"] = 9
alumno["aprobado"] = True
print(alumno)
print("------------------ejercicio 12 ---------------\n")
colores = {"rojo": "red", "azul": "blue", "verde": "green"}
for clave, valor in colores.items():
    print(f" el color  es => {clave}, y su valor => {valor} ")