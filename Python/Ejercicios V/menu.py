import os, time, ejercicio1, ejercicio2, ejercicio3, ejercicio4, ejercicio5


def limpiar():
    time.sleep(3)
    os.system("cls")


def menu():
    salir = False
    while salir == False:

        print("""
               Escribe una opcion para seleccionar ejercicio:

               0.Salir

               1.Realiza un ejercicio que me permita convertir números binarios en enteros y viceversa. Utiliza una función

               2.Realiza un ejercicio que te permita introducir una frase y te muestre el número de veces que se repiten las letras.

               3.Realiza un ejercicio que te indique si el año que introduces es bisiesto. Utiliza una función.

               4.Realiza un ejercicio que te pida un fichero, lea linea a linea y las copie en un nuevo fichero.
               """)
        menuopc = input("Introduce una opcion")

        if menuopc == "0":
            print("Adios")
            salir = True
            continue
        if menuopc == "1":
            print("Has seleccionado el Ejercicio 1, empezemos:")
            print("""Que quieres hacer, pasar un decimal a binario o un binario a decimal:
                    1. Decimal a binario.
                    2. Binario a decimal.
                  """)
            opcion = int(input("Introduce una opcion"))
            if opcion == 1:
                ejercicio1.ejer1_2()
            if opcion == 2:
                ejercicio1.ejer1_1()
            limpiar()
            continue
        if menuopc == "2":
            print("Has seleccionado el Ejercicio 2, empezemos:")
            ejercicio2.ejer2()
            limpiar()
            continue
        if menuopc == "3":
            print("Has seleccionado el Ejercicio 3, empezemos:")
            ejercicio3.ejer3()
            limpiar()
            continue
        if menuopc == "4":
            print("Has seleccionado el Ejercicio 4, empezemos:")
            ejercicio4.ejer4()
            limpiar()
            continue
        if menuopc == "5":
            print("Has seleccionado el Ejercicio 5, empezemos:")
            ejercicio5.ejer5()
            limpiar()
            continue

        else:
            print("Error: Has introducido una opcion no valida")
            limpiar()


menu()