def ejer18():
    cad1 = input("Introduce palabras separadas por espacios")
    num = int(input("Introduce un numero"))
    cad1 = cad1.split(" ")
    e = int(0)
    contador = int(0)
    for i in cad1:
        prueba2= len(cad1[e])
        if prueba2  > num:
            contador = contador+1
        e=e+1
    print ("Hay",contador,"palabras con mas de",num,"caracteres" )
ejer18()