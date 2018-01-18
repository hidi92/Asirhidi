import os
def limpiar():
    os.system("cls")
def ejer9():
    listanombres= [] #iniciamos la lista de nombres
    listatelefonos= [] #iniciamos la lista de telefonos
    contador =int(0) #iniciamos el contador que recorre la lista
    ciclo1 = True #iniciamos valor del bucle primario

    while ciclo1 == True: #Iniciamos bucle primario
        ciclo2 = True #iniciamos valor del bucle secundario
        while ciclo2 == True: #Iniciamos bucle secundario
            ciclo2 = False #paramos bucle secundario
            nombres = input("Introduce un nombre")
            telefonos = input("Introduce un telefono")
            for e in listatelefonos: #creamos bucle con posicione de la lista telefonos

                if telefonos == listatelefonos[contador]: #recorremos la lista comparando telefonos 1 a 1
                    print("Numero repetido, vuelve a intentarlo")
                    limpiar()
                    ciclo2 = True #Iniciamos bucle secundario en caso de que un telefono se repita
                contador = contador + 1 #Vamos sumando 1 al contador
            contador=0 #Reiniciciamos el contador a 0

        listanombres.append(nombres) #Añadimos nombre a la lista de nombres
        listatelefonos.append(telefonos) #Añadimos telefonos a la lista de telefonos
        ciclo2 = True #Iniciamos otro bucle secundario
        while ciclo2 == True:
            salir = input("Escribe 'n' para mostrar agenda | Escribe 's' para añadir otro contacto")
            if salir == "s":
                ciclo1 = True #Reiniciamos el bucle primario
                ciclo2 = False #Paramos bucle secundario
                limpiar()
            elif salir=="n":
                limpiar()
                for i in listatelefonos:
                    print("Nombre: ",listanombres[contador])
                    print("Telefono: ",listatelefonos[contador])
                    contador = contador + 1
                contador = 0
                ciclo1 = False #Paramos bucle primario
                ciclo2 = False #Paramos bucle secundario
            else:
                limpiar()
                print("Has introducido una opcion incorrecta, vuelve a intentarlo")
                ciclo2 = True #Reiniciamos el bucle secundario
ejer9()