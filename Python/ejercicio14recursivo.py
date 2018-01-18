def factorial(n=int(input("¿Cuantos numeros quieres introducir?"))):
    print(n)
    if n==1:
        print(1)
    else:
        print(n * factorial(n-1))
factorial()
