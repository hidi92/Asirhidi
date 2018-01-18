def ejer17():
    cad1 = input("Introduce numeros o caracteres y separalos con espacios")
    cadenadesordenada = list(cad1)
    cadenaordenada = list(cad1)
    cadenaordenada.sort(reverse=True)
    print("Aqui esta tu lista:",cadenadesordenada)
    e=int(-1)
    for i in cadenadesordenada:
        e = e +1
        if cadenadesordenada[e] == cadenaordenada[0]:
            print ("El caracter mayor es:" ,cadenaordenada[0] , " Y la esta en la posicion:", e)

ejer17()