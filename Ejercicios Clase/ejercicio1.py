def nummayor(x=int(input("¿Cuantos numeros quieres introducir?"))): #Definimos la funcion
    lista1=[] #Declaramos una array vacia
    for i in range(x): #Creamos un ciclo que va desde 0 hasta el valor que le hayamos asignado a x
        numlista= (int(input("Introduce el numero: "+ str(i+1)))) #Creamos variable  para introducir los numeros a comparar
        lista1.append(numlista) #Añadimos a la array el valor del numero a comparar
    lista1.sort(reverse=True) #Ordenamos de mayor a menor los elementos de la array
    print("El numero mayor es: ",lista1[0]) #Imprimimos el primer elemento de la array que tendra el numero mas grande al estar ordenado de mayor a menor.
nummayor() #Ejecutamos la funcion.