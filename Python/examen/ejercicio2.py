def ejer2():
    frase=input("introduce una frase").split(" ")
    longitudcadena=len(frase)
    for i in range (longitudcadena):
        letras = list(frase[i])
        letras[0]=letras[0].upper()
        palabramayus=("".join(letras))
        print(palabramayus)

ejer2()