from calculadora import *

""" def familias(nombre,*args):
  print("NOMBRES")
  print(f"me llamo {nombre}")
 
  for x in args:
    print(x)
     """
    
#familias("alex","joseft",45)
    
  
# Principal
print("Calculadora básica")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Input de opciones
opcion = input("Elige una de las opciones: ")

# Declaro las variables y pido valor.
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

# Condicional para ejecutar funciones
if opcion == "1":
    print("Resultado: ", sumar(num1, num2))
elif opcion == "2":
    print("Resultado: ", restar(num1, num2))
elif opcion == "3":
    print("Resultado: ", multiplicar(num1, num2))
elif opcion == "4":
    print("Resultado: ", dividir(num1, num2))
else:
    print("Opción inválida.")
