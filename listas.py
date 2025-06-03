matrix = [[1,2],[34,6],[5,9],[21,567,9]]
#print(type(matrix))
print(matrix[0][1])
print("los elementos aparecen : ->", matrix.count([1,2]),"ves")#cuenta cuantas veces aparece un elemento
#slincing
print(matrix[::3])
matrix.append([111,70])#agrega al final
print(matrix)
msg = [1,3,0]
list = [ "a","d","df"]
final =msg + list
print(len(final))#cuenta

list.insert(1,"fg")#inserta la posicion dada
print(list)
list.extend(["😂","😂", "😂"])#concatena otra lista
print(list)
list.remove("a")#borra la primera ves que encuentra el caracter
print(list)
listado =list.pop()#elimina el ultimo element y lo devuelve
print(listado)
numeros = [1,4,2,9,0,6,7,3]
copia_list = numeros[:]#copia una lista
print(f"esta es una copia de {numeros}")
numeros.sort()#ordena pero modifica la lista no la devuelve
print(numeros)
numeros_finales = sorted(numeros)#hace una copia de la lista y la devuelve
print(numeros_finales)

print("-------LIST COMPREHESION------------")

list_id = [ "a","d","df"]
grados,curso,direcion =list_id
print(list_id)
my_lista = [li.upper() for li in list_id ]
print(id(my_lista))

print(id(list_id))
print("-----ejercicio----------")
lista1 = ["Daniel",39851255,True]
lista2 = ["Juan",38555111,False]

lista1[2] ="movies"#agregar un elemento de manera basica
lista3 = lista1+lista2
print(lista3)