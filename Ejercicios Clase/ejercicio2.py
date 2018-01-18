def contarcadena(cad=input("¿Introduce un texto?")): #Definimos la funcion
    contador=0
    minus = cad.lower()
    sep = list(minus)
    for i in sep:
        contador=contador+1
    print ("Tu cadena tiene" , contador, "caracteres")
contarcadena()