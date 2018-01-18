import os, time
def limpiar():
    time.sleep(2)
    os.system("cls")
def fecha():
    salir = False
    while salir == False:


        menuopc = input("Introduce un numero del 1 al 12 para decirte el mes correspondiente, introduce 0 para salir")

        if menuopc == "0":
            print("Adios")
            salir = True
            continue
        if menuopc == "1":
            print ("El mes es Enero")
            limpiar()
            continue
        if menuopc == "2":
            print ("El mes es Febrero")
            limpiar()
            continue
        if menuopc == "3":
            print ("El mes es Marzo")
            limpiar()
            continue
        if menuopc == "4":
            print ("El mes es Abril")
            limpiar()
            continue
        if menuopc == "5":
            print ("El mes es Mayo")
            limpiar()
            continue
        if menuopc == "6":
            print ("El mes es Junio")
            limpiar()
            continue
        if menuopc == "7":
            print ("El mes es Julio")
            limpiar()
            continue
        if menuopc == "8":
            print ("El mes es Agosto")
            limpiar()
            continue
        if menuopc == "9":
            print ("El mes es Septiembre")
            limpiar()
            continue
        if menuopc == "10":
            print ("El mes es Octubre")
            limpiar()
            continue
        if menuopc == "11":
            print ("El mes es Noviembre")
            limpiar()
            continue
        if menuopc == "12":
            print ("El mes es Diciembre")
            limpiar()
            continue
        else:
            print("Error: Has introducido una opcion no valida")
            limpiar()
fecha()