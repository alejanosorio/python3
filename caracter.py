caracter = input("intro caracter :")
if caracter.isupper():
    print(f"{caracter } es MAYUSCULA")
elif caracter.islower():
    print(f"{caracter} es minuscula")
elif caracter.isnumeric():
    print(f"{caracter} es un numero")
else:
    print("es un caracter especial") 