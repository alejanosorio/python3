""" Ejercicio 1: Número positivo, negativo o cero
Descripción: Leer un número e indicar si es positivo, negativo o cero.
Ejercicio 2: Mayor de dos números
Descripción: Leer dos números e indicar cuál es mayor o si son iguales.
Ejercicio 3: Verificar si un número es par o impar
Descripción: Leer 5 números y para cada uno decir si es par o impar.
Ejercicio 4: Sumar 10 números
Descripción: Realizar la sumatoria del 1 al 10 y mostrar la suma total.
Ejercicio 5: Tabla de multiplicar
Descripción: Ingresar un número y mostrar su tabla de multiplicar del 1 al 10.
Ejercicio 6: Ingresar contraseña
Descripción: Solicitar al usuario que ingrese una contraseña. Repetir el pedido mientras la
contraseña ingresada no sea correcta. La contraseña válida es "informatorio".
Ejercicio complementario: Contador de positivos y negativos
Descripción: Leer números hasta que el usuario ingrese 0. Contar cuántos son positivos y
cuántos negativos."""

print("Ejercicio 1:\n ")
numero = int(input("introduce un numero :\n"))

if numero < 0:
    print("el numero es negativo")
elif numero > 0:
    print("numero positivo")
else :
    print("el numero es cero")

print("Ejercicio 2:\n ")
mayor =int(input("imtro un numero :\n "))
menor =int(input("imtro otro numero :\n "))

if mayor > menor:
    print(f"el numero {mayor} es mayor que {menor}")
elif mayor < menor:
     print(f"el numero {mayor} es menor que {menor}")
else:
    print(f"el numero {mayor} y el {menor} son iguales")    
print("Ejercicio sumar del 1 al 10:\n ")    
suma = 0
numero = 1

while numero <= 10:
    suma += numero
    numero += 1

print(f"La suma del 1 al 10 es:{ suma}")

print("Ejercicio 3:\n ")

for x in range(6):
    if x % 2 ==0:
        print(f"numero par {x}")
    else:
        print(f"numero impar {x}")
        
print("Ejercicio 6:\n ")


while True:
   entrada = input("ingrese password :\n")
   if entrada =="informatorio":
       print("inicio sesion....")
       break
   else:
       print("ingreso incorrecto!")
    