

#Sistema de seguridad de acceso
usuario = ""
clave = ""

while usuario != "admin" or clave != "123":
    usuario = input("Introduzca su usuario: ")
    clave = input("Introduzca su clave: ")
    if usuario == "admin" and clave == "123":
        print("¡Bienvenido!")
    else:
        print("Acceso denegado, inténtelo otra vez")
