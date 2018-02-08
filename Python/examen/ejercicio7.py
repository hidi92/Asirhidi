def ejer7():
    listanum=[]
    cantidad=int(input("¿cuantos numeros vas a introducir?"))
    suma=int(0)
    for i in range (cantidad):
        numero = int(input("introduce un numero"))
        suma = suma + numero
        listanum.append(numero)
    listanum.sort()
    print("numeros ordenados ascendentemente",listanum)
    print("la suma de los numeros es:",suma)


ejer7()