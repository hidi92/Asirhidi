def ejer8():
    derecho= []
    reves= []
    valor = True
    while valor == True:
        numero = int(input("Introduce un numero"))
        if numero == 0:

            reves.sort(reverse=True)
            print("Al derecho",derecho)
            #print(reves)
            print("Al reves", reves)
            valor = False
        else:
            derecho.append(numero)
            reves.append(numero)

ejer8()


