def ejer1_1():
    numero = list(input("Introduce un numero binario"))
    contadordenumeros = len(numero)
    contadorexponente = int(contadordenumeros-1)
    #print (contadorexponente)
    sumadetodo = int(0)
    for i in range (0,contadordenumeros):
        sumadetodo = sumadetodo + (int(numero[i])*(2**contadorexponente))
        contadorexponente = contadorexponente -1
    print ("Tu numero en decimal es:",sumadetodo)
#ejer1_1()
def ejer1_2():
    numero = int(input("Introduce un numero entero"))
    division = int(numero / 2)
    resto = str(numero % 2)
    contador_resto = resto
    resto = str(division % 2)
    contador_resto = contador_resto + resto

    while (division >= 2):
        division = int(division / 2)
        resto = str(division % 2)
        contador_resto = contador_resto + resto

    contador_resto.split()
    contador_resto = ''.join(reversed(contador_resto))
    print("Tu numero en binario es:",contador_resto)
#ejer1_2()