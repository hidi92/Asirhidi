def ejer3():
    listanombres=[]
    listanotas=[]
    suma=int(0)
    numeroalumnos=int(input("Introduce el numero de alumnos a introducir"))
    for i in range (numeroalumnos):
        nombre = input("Introduce el nombre del alumno")
        listanombres.append(nombre)
        nota=int(input("Introduce la nota del alumno"))
        listanotas.append(nota)
        suma = suma + nota
    media = float(suma/numeroalumnos)
    for e in range (numeroalumnos):
        if listanotas[e] <= media:
            if listanotas[e] < 5:
                print(listanombres[e],"ha obetinido la nota de insuficiente, y esta por debajo de la media",media)
                continue
            if listanotas[e] < 6:
                print(listanombres[e],"ha obetinido la nota de suficiente, y esta por debajo de la media",media)
                continue
            if listanotas[e] < 7:
                print(listanombres[e],"ha obetinido la nota de bien, y esta por debajo de la media",media)
                continue
            if listanotas[e] < 8:
                print(listanombres[e],"ha obetinido la nota de notable, y esta por debajo de la media",media)
                continue
            if listanotas[e] >= 9:
                print(listanombres[e],"ha obetinido la nota de sobresaliente, y esta por debajo de la media",media)
                continue
        else:
            if listanotas[e] >= media:
                if listanotas[e] < 5:
                    print(listanombres[e], "ha obetinido la nota de insuficiente, y esta por encima de la media", media)
                    continue
                if listanotas[e] < 6:
                    print(listanombres[e], "ha obetinido la nota de suficiente, y esta por encima de la media", media)
                    continue
                if listanotas[e] < 7:
                    print(listanombres[e], "ha obetinido la nota de bien, y esta por encima de la media", media)
                    continue
                if listanotas[e] < 8:
                    print(listanombres[e], "ha obetinido la nota de notable, y esta por encima de la media", media)
                    continue
                if listanotas[e] >= 9:
                    print(listanombres[e], "ha obetinido la nota de sobresaliente, y esta por encima de la media",
                          media)
                    continue
ejer3()