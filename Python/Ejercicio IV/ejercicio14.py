def ejer19():
    cad1 = input("Introduce palabras separadas por espacios")
    letra = input("Introduce un caracter")
    cad1 = cad1.split(" ")
    e = int(0)
    cadenafinal=[]
    contador = int(0)
    for i in cad1:
        primercaracter= (cad1[e][0])
        if primercaracter  == letra:
            cadenafinal.append(cad1[e])
        #print(prueba2)
        e=e+1
    print ("Estas son las palabras que empiezan por",letra,":",cadenafinal)
ejer19()