def ejer15():
  pacientes_origen=open("pacientes_origen.txt","r")
  pacientes_destino=open("pacientes_destino.txt","a")
  for linea in pacientes_origen:
    cadena_linea=linea.split(";")
    if int(cadena_linea[1]) > 20 and cadena_linea[2].strip("\n") == "no":
      pacientes_destino.write(linea)
  print('Archivo "pacientes_destino.txt" escrito correctamente')
  pacientes_origen.close()
  pacientes_destino.close()
ejer15()
