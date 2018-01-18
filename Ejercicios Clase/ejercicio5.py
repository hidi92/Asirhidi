def palindromo():
    palin = input("Introduce un numero")
    normal = list(palin)
    reves = list(palin)
    reves.reverse()
    if normal==reves:
        print ("Es palindromo")
    else:
        print("No es palindromo")
palindromo()