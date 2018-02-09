"""def ejer5():
    nombres=["david","diego","davido","fernando"]
    cantidad_nombres = len(nombres)
    for i in range(cantidad_nombres):
        lista = list(nombres[i])
        cantidad_separado = len(lista) - 1
        if lista[0] == "d" and lista[cantidad_separado] == "o":
            print("".join(lista))

print (ejer5())"""

def ejer5bis():
    import re
    nombres=("hidi1992@gmail.com")
    if re.match(".*@.*\..*", nombres):
        print(nombres)


(ejer5bis())