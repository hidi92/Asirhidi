def tablamulti():
    numero = int(input("Introduce un numero"))
    numero1 = numero
    for i in range (11):
        numero=numero1
        numero=numero*i
        print(numero1 , "x", i, "=" , numero)
tablamulti()

