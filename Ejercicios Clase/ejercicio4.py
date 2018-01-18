def sumarymultiplicar():  # Definimos la funcion
    listanum=[]
    suma = 0
    multiplicacion = 1
    x=int(input("¿Cuantos numeros quieres introducir?"))
    for i in range(x):
        num = int(input("Introduce un numero"))
        listanum.append(num)
    opcion = int(input("Introduce 1 para sumarlos o 2 para multiplicarlos"))
    conta=len(listanum)

    if opcion == 1:
        for i in listanum:
            suma = suma + i
        print(suma)
    elif opcion == 2:
        for e in listanum:
            multiplicacion = (multiplicacion * int(e))
        print(multiplicacion)

sumarymultiplicar()

