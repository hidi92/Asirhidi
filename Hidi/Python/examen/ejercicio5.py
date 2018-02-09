def ejer5():
    listapalabras=input("introduce una lista de palabras separadas por espacios ").split(" ")
    numero=int(input("introduce un numero"))
    longitudcadena=len(listapalabras)
    for i in range (longitudcadena):
        longitudpalabra=len(listapalabras[i])
        if longitudpalabra > numero:
            print(listapalabras[i],"tiene mas de",numero,"caracteres")

ejer5()