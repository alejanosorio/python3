"""
words = ("hola mundo","que tal","welcome python")

for i,word in enumerate(words):
    print(i,word)
print("----------------------------")  
#for anidado 
letras =["a","b","c"]
nums = [1,4,5,2]
for i in letras:
    for x in nums:
        print(i,x)
""" 
print("----------suma de numeros----------")
numeros_sumados = [2,4,5,7,88,9,3]
suma =0
for x in numeros_sumados:
    suma += x
print(f"la suma es {suma}")


# 
print("--------------imprimir numeros pares-------------")
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
for x in range(0,21,2):
    print(x)
   
print("\nEjercicio 1:")

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
numeros = [15, 5, 25, 10, 20]
num = max(numeros)
print(num)
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")