import os, time
def limpiar():
    time.sleep(2)
    os.system("cls")
def menu():
    salir = False
    while salir == False:

        print ("""
               Escribe una opcion para seleccionar ejercicio:
               
               0.Salir
               
               1.Realiza un ejercicio que pida por teclado un número y muestre el mes correspondiente.
                 Muestra el mensaje oportuno si el número es mayor de 12. Se dejará de pedir número cuando pulses 0.
               
               2.Realiza un ejercicio que muestre la tabla de multiplicar del número que introduzcas por teclado.
               
               3.Realiza un ejercicio que te pida números hasta que introduzcas el 0, a continuación te mostrará
                 todos los números introducidos ordenados de mayor a menor y viceversa.
               
               4.Realiza una agenda que te permita introducir nombres y sus teléfonos, hasta que quieras
                 finalizar. No se pueden repetir teléfonos.
               
               5.Realiza un ejercicio que compare 2 listas. Las listas las introduces por teclado. 
                 Crea una función para ello. Si son iguales, que lo indique.
               
               6.Realiza un ejercicio que pida un número "n" y un caracter y te muestre ese caracter "n" veces repetido 
                 en la misma línea.
               
               7.Realiza un ejercicio que te pida una lista de números y te muestre en cada línea ese mismo número en asteriscos.
               
               8.Realiza un ejercicio que te pida un numero y te muestre.Por ejemplo, si metes 5:
                    *
                    **
                    ***
                    ****
                    *****
               
               9.Realiza un ejercicio que calcule el factorial de un número. Utiliza una función.
               
               10.Realiza un ejercicio que pida tu nombre y tus apellidos y me los muestre al revés. 
                  Utiliza una función.
               
               11.Realiza un programa que pida un texto y me devuelva ese mismo texto sin vocales.
               
               12.Realiza un ejercicio que nos muestre la posición del mayor de los números o caracteres que introducimos.
               
               13.Realiza un ejercicio que pida una lista de palabras y un número y te indique 
                  qué palabras tienen mas de "n" caracteres.
               
               14.Realiza un ejercicio que a partir de una lista de nombres que le pases y de una letra 
                  que también pases, devuelva todos los nombres que comiencen por esa letra.
                  
               15.Dado un fichero “Pacientes.txt”, que contiene la información de unos pacientes 
                  en el formato (nombre edad diabético si/no), generar un nuevo fichero que contenga 
                  los pacientes que tienen más de 20 años y no son diabéticos.
                   
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
        if menuopc == "15":
            print ("Has seleccionado el Ejercicio 15, empezemos:")
            import ejercicio15
            limpiar()
            continue

        else:
            print("Error: Has introducido una opcion no valida")
            limpiar()
menu()