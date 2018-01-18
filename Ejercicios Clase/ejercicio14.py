def ejer14():
    numero = int(input("Introduce un numero"))
    numero=numero+1
    factorial=1
    for i in range (1,numero):
        factorial = factorial * i
    print("El factorial de",numero - 1, "es:", factorial)
ejer14()