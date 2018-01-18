def ejer10():
    cad1 = input("Introduce una cadena, separa las palabras con espacios.")
    cad2 = input("Introduce otra cadena, separa las palabras con espacios.")
    cad1 = cad1.split(" ")
    cad2 = cad2.split(" ")
    if cad1 == cad2:
        print("Las listas introducidas son iguales")
    else:
        print("Aqui estan las listas introducidas:")
        print("Lista 1: ", cad1)
        print("Lista 2: ", cad2)
ejer10()