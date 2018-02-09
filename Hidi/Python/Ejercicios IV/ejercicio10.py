def ejer15():
    cad1 = input("Introduce tu nombre y apellidos, separalos con espacios")
    cad1 = cad1.split(" ")
    cad1.reverse()
    e = 0
    for i in cad1:
        print(cad1[e])
        e = e+1
ejer15()
