def ejer1():
    numero = list(input("Introduce un numero binario"))
    contadordenumeros = len(numero)
    contadorexponente = int(contadordenumeros-1)
    #print (contadorexponente)
    sumadetodo = int(0)
    for i in range (0,contadordenumeros):
        sumadetodo = sumadetodo + (int(numero[i])*(2**contadorexponente))
        contadorexponente = contadorexponente -1
    print ("Tu numero en decimal es:",sumadetodo)
#ejer1()
