def ejer12():
    asterix="*"
    numeros = input("Introduce una lista de numeros separados por espacios")
    numeros = numeros.split(" ")
    for i in numeros:
        e = int(i)
        print('a' * e)
ejer12()