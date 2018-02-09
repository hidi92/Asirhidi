def ejer1():
    import re
    correo=input("Introduce un correo")
    if re.match(".*@[0-9A-z]*(\.)[0-9a-z]*",correo):
        print("Correo correcto")
    else:
        print("Correo incorrecto")
ejer1()