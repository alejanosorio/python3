def crear_libro(titulo,author,año):
    return {"titulo":titulo,"author":author,"año":año}
def agregar_libro(biblioteca,libro):
    return biblioteca.append(libro)
def buscar_libro(biblioteca,titulo):
    for libro in biblioteca:
        if libro ["titulo"]== titulo:
            return libro
    return "no existe ese libro"
def mostrar_libro(biblioteca):
    for libro in biblioteca:
        print(f'Titulo : {libro['titulo']}, Author : {libro['author']}, Año : {libro['año']}')