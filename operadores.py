print(3 / 7 // 8 + 4 **6 -2)
print("Python " * ( 3 ** 2))
#compara orden alfabetico ASCII
print("hello" > "world")
print("hello" < "world")
print("hello" == "hello")
print("HELLO" >= "hello")
print("------LOGICOS-----")
print(3 > 5 and 4 == 4)#false true=false
print(3 > 5 or 6 > 5)#false true= true
print( not ("hello" > "hola"))

"""
and	Devuelve True si ambos elementos son True -	True and True = True
or	Devuelve True si al menos un elemento es True-	True or False = True
not	Devuelve el contrario, True si es Falso y viceversa	not True = False
 """
print("-------operador AND-----------")
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

print("-----------Operador OR----------")
print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False
print("-------- operador NOT----------")
print(not True)  # False
print(not False) # True
print(not not not not True) # True