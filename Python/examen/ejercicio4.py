def ejer4():
    archivo1 = open("archivo1.txt","r")
    archivo2 = open("archivo2.txt", "r")
    archivo3 = open("archivo3.txt", "r")
    archivo4 = open("archivo4.txt", "r")
    archivodestino= open("archivodestino.txt", "a")
    for linea in archivo1:
        cadenalinea = linea.split(" ")
        longitudcadena=len(cadenalinea)
        for i in range (longitudcadena):
            if cadenalinea[i]=="script":
                archivodestino.write(linea)
                archivodestino.write("\n")
    for linea in archivo2:
        cadenalinea = linea.split(" ")
        longitudcadena=len(cadenalinea)
        for i in range (longitudcadena):
            if cadenalinea[i]=="script":
                archivodestino.write(linea)
                archivodestino.write("\n")
    for linea in archivo3:
        cadenalinea = linea.split(" ")
        longitudcadena=len(cadenalinea)
        for i in range (longitudcadena):
            if cadenalinea[i]=="script":
                archivodestino.write(linea)
                archivodestino.write("\n")

    for linea in archivo4:
        cadenalinea = linea.split(" ")
        longitudcadena=len(cadenalinea)
        for i in range (longitudcadena):
            if cadenalinea[i]=="script":
                archivodestino.write(linea)
                archivodestino.write("\n")

ejer4()