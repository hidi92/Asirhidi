def ejer2():
    texto=input("Introduce un texto")
    abecedario = list("abcdefghijklmnñopqrstuvwxyz")
    for i in abecedario:
        contar = (texto.count(i))
        if contar > 0:
            print ("La letra", i , "Se repite",contar,"veces")
ejer2()