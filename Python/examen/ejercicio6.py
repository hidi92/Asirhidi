def ejer6():
    listafrase = input("introduce una frase").split(" ")
    letra = input("introduce una letra")
    #longitudcadena = len(listafrase)
    for i in listafrase:
        for e in i:
            e = e.lower()
            if e == letra:
                print("esta palabra",i,"empieza por",letra)
            break

ejer6()