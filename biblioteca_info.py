from modulos.biblioteca import crear_libro,agregar_libro,buscar_libro,mostrar_libro

libreria_del_info = []
libro_1 = crear_libro("de la tierra a la luna","julio verne",1971)
libro_2 = crear_libro("eloquent javascript","Marijn Haverbeke",2011)
libro_3 = crear_libro("python para todos","gonzales duque",2015)

agregar_libro(libreria_del_info,libro_1)
agregar_libro(libreria_del_info,libro_2)
agregar_libro(libreria_del_info,libro_3)

mostrar_libro(libreria_del_info)
libro_encontrado = buscar_libro(libreria_del_info,"de la tierra a la luna")
print(libro_encontrado)