import os, time
def limpiar():
    time.sleep(2)
    os.system("cls")
def menu():
    salir = False
    while salir == False:

        print ("""
               Escribe una opcion para seleccionar ejercicio
               0.Salir
               1.Ejercicio numero mayor
               2.Ejercicio contar caracteres
               3.Ejercicio contar vocales
               4.Ejercicio sumar y multiplicar
               5.Ejercicio Numeros palindromos
               6.Ejercicio mostrar mes
               7.Ejercicio tabla multiplicar
               8.Ejercicio ordenar numeros
               9.Ejercicio agenda
               10.Ejercicio comparar listas
               11.Ejercicio multiplicar caracter
               12.Ejercicio lista de asteriscos
               13.Ejercicio suma de asteriscos
               13.Ejercicio factorial de un numero
               """)
        menuopc = input("Introduce una opcion")

        if menuopc == "0":
            print("Adios")
            salir = True
            continue
        if menuopc == "1":
            print ("Has seleccionado el Ejercicio 1, empezemos:")
            import ejercicio1
            limpiar()
            continue
        if menuopc == "2":
            print ("Has seleccionado el Ejercicio 2, empezemos:")
            import ejercicio2
            limpiar()
            continue
        if menuopc == "3":
            print ("Has seleccionado el Ejercicio 3, empezemos:")
            import ejercicio3
            limpiar()
            continue
        if menuopc == "4":
            print ("Has seleccionado el Ejercicio 4, empezemos:")
            import ejercicio4
            limpiar()
            continue
        if menuopc == "5":
            print ("Has seleccionado el Ejercicio 5, empezemos:")
            import ejercicio5
            limpiar()
            continue
        if menuopc == "6":
            print ("Has seleccionado el Ejercicio 6, empezemos:")
            import ejercicio6
            limpiar()
            continue
        if menuopc == "7":
            print ("Has seleccionado el Ejercicio 7, empezemos:")
            import ejercicio7
            limpiar()
            continue
        if menuopc == "8":
            print ("Has seleccionado el Ejercicio 8, empezemos:")
            import ejercicio8
            limpiar()
            continue
        if menuopc == "9":
            print ("Has seleccionado el Ejercicio 9, empezemos:")
            import ejercicio9
            limpiar()
            continue
        if menuopc == "10":
            print ("Has seleccionado el Ejercicio 10, empezemos:")
            import ejercicio10
            limpiar()
            continue
        if menuopc == "11":
            print ("Has seleccionado el Ejercicio 11, empezemos:")
            import ejercicio11
            limpiar()
            continue
        if menuopc == "12":
            print ("Has seleccionado el Ejercicio 12, empezemos:")
            import ejercicio12
            limpiar()
            continue
        if menuopc == "13":
            print ("Has seleccionado el Ejercicio 13, empezemos:")
            import ejercicio13
            limpiar()
            continue
        if menuopc == "14":
            print ("Has seleccionado el Ejercicio 14, empezemos:")
            import ejercicio14
            limpiar()
            continue
        else:
            print("Error: Has introducido una opcion no valida")
            limpiar()
menu()