"""
    Ejercicios complementaros: Estructuras de datos
1-Crear un diccionario con los nombres de tres frutas y sus respectivos
precios y mostrar el diccionario completo.
2-Crear una lista con los nombres de tres ciudades y agregar una cuarta
ciudad al final de la lista.
3-Crear una lista con los nombres de tres países y mostrar el segundo
país de la lista.
4-Crear un diccionario con los nombres de tres personas y sus
respectivas edades. Mostrar la edad de la tercera persona en el
diccionario.
5-Crear un set/conjunto con los números del 1 al 10 y mostrar el número
más grande en el conjunto.
6-Crear un set/conjunto con los números impares del 1 al 10 y mostrar el
número de elementos en el conjunto.
7-Crear un diccionario con los nombres de tres ciudades y sus
respectivas poblaciones. Agregar una cuarta ciudad al diccionario con
su respectiva población. Mostrar el diccionario resultante.
8-Crear una lista con los números del 1 al 10 y mostrarlos en orden
inverso.
9-Crear una lista con los nombres de tres países y ordenar la lista en
orden alfabético. Mostrar la lista resultante.
10-Crear una lista con los nombres de tres frutas y eliminar la segunda
fruta de la lista. Mostrar la lista resultante.
11-Crear una lista con los nombres de tres animales y agregar una cuarta
animal al principio de la lista. Mostrar la lista resultante.
12-Crear una lista con los nombres de tres países y reemplazar el
segundo país de la lista por otro país. Mostrar la lista resultante.
13-Crear una lista con los nombres de tres colores y agregar dos colores
más al final de la lista. Mostrar la lista resultante.
14-Crear una tupla con los números del 1 al 5 y mostrar la suma de todos los elementos de la tupla."""

print("------ ejercicio 4 -----------------")
personas = {"pepe":45,"jon":29,"luis":65}
una_persona =personas.get("luis")
print(f"la edad de la tercera persona es : {una_persona}")

print("------ ejercicio 7 -----------------")
citys = {
  "bs as": 10000000,
  "resistencia": 150000,
  "rosario": 200000
}

citys.update({"la banda": 100000})

print(citys)



print("------ ejercicio 8 -----------------")
my_numeros = [1,2,3,4,5,6,7,8,9,10]
my_numeros.reverse()
print(my_numeros)


print("------ ejercicio 9 -----------------")
paises = ["rusia","mexico","suiza"]
paises.sort()
print(paises)

print("------ ejercicio 10 -----------------")

fruta = ["pera","banana","sandia"]
fruta.pop(1)
print(fruta)


print("------ ejercicio 11 -----------------")
animals = ["vaca","tigre","venado"]
animals.insert(0,"lion")
print(animals)

print("------ ejercicio 12 -----------------")
paises = ["eeuu","grece","france","ucrkania"]
paises[1] = "chine"
print(paises)


print("------ ejercicio 13 -----------------")

colores = ["red","black","green"]
agregados  = ["yellow","white"]
colores.extend(agregados)
print(colores)


print("------ ejercicio 14 -----------------")

my_tuple = (1,2,3,4,5)
sum = 0
for x in my_tuple:
    sum += x
print(sum)