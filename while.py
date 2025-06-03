
contador = 0
while contador < 20:
    contador +=1
    if contador % 2 == 0:
        #no muestra los numeros pares
      break
    print(contador) 
else:
    print("programa terminado")
    
numero = -1
while numero <=0:
    try:
        numero = int(input("intro numero positivo : \n"))
        
    except:
        print("intro solo numeros")

print(f"el numero es : {numero}\n")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
num = 0
while num <= 10:
    num +=1
    print(num)
    
     
