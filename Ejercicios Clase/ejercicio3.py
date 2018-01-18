def decirvocales(x=input("Introduce un texto")):
    minus=x.lower()
    contadorvocal=[]
    contadorconsonante = []
    contadornum = []
    contadorespacios = []
    sep=list(minus)

    for i in sep:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            contadorvocal.append(i)
        elif i == "b" or i == "c" or i == "d" or i == "f" or i == "g" or i == "h" or i == "j" or i == "k" or i == "l" or i == "m" or i == "n" or i == "ñ" or i == "o" or i == "p" or i == "q" or i == "r" or i == "s" or i == "t" or i == "v" or i == "w" or i == "x" or i == "y" or i == "z":
            contadorconsonante.append(i)
        elif i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
            contadornum.append(i)
        else:
            contadorespacios.append(i)

    print("Hay",len(contadorvocal) ,"vocales")
    print("Hay",len(contadorconsonante),"consonantes")
    print("Hay",len(contadornum),"numeros")
    print("Hay", len(contadorespacios), "espacios o simbolos")

decirvocales()