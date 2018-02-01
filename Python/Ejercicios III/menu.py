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
               
               1.Realiza un ejercicio que me indique el mayor de los números que le pasas. 
                 Utiliza una función que simule la función max().
                 
               2.Realiza un ejercicio que simule la función len(). Pida una frase y con una función te devuelva su longitud.
               
               3.Realiza un ejercicio que te indique el número de vocales, consonantes o números que has introducido por teclado.
                 Utiliza una función.
                 
               4.Realiza un ejercicio que te sume y te multiplique, los números que pasas por teclado.
               
               5.Realiza un ejercicio que reconozca palíndromos. Utiliza una función.    
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

        else:
            print("Error: Has introducido una opcion no valida")
            limpiar()
menu()