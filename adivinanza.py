import random
numero_secreto = random.randint(1,100)
intentos = 0
while True:
    adivinanza = input("adivina el numero :")
    if not adivinanza.isdigit():
        print("intro numero valido")
        continue 
    adivinanza =int(adivinanza)
    intentos += 1
    if adivinanza < numero_secreto:
        print("demasiado bajo prueba mas alto :")
    elif adivinanza > numero_secreto:
        print("demasiado alto pueba mas bajo :")
    else:
        print(f"felicitaciones adivinaste el numero en {intentos} intentos :") 
        break
print("gracias por jugar hasta la proxima!!!")