def ejer4():
    archivo_ejer4_origen = open("archivo_ejer4_origen.txt", "r")
    archivo_ejer4_destino = open("archivo_ejer4_destino.txt", "a")
    for linea in archivo_ejer4_origen:
        cadena = linea.split(" ")
        archivo_ejer4_destino.write(linea)
    archivo_ejer4_origen.close()
    archivo_ejer4_destino.close()
    print("Archivo copiado correctamete")
#ejer4()