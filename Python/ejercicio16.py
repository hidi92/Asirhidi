def decirvocales(x=input("Introduce un texto")):
    minus=x.lower()
    contadorvocal=[]
    sep=list(minus)

    for i in sep:
        contadorvocal.append(i)
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            #print(contadorvocal)
            #print(i)
            contadorvocal.remove(i)
    cadena = " ".join(contadorvocal)
    print(cadena)

decirvocales()