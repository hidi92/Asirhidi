import os
def limpiar():
    os.system("cls")
def fecha():
    salir = False
    while salir == False:

        meses = ["Adios","enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre",]
        menuopc = int(input("Introduce un numero del 1 al 12 para decirte el mes correspondiente, introduce 0 para salir"))
        e=int(0)
        if menuopc == 0:
            print("Adios")
            salir == True
            break
        if menuopc <0 or menuopc >12:
            print("Error: Has introducido una opcion no valida")
        else:
            for i in meses:
                e = e + 1
                if menuopc == e:
                    print(meses[e])
                    salir = False
limpiar()
fecha()