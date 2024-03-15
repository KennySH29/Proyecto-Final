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

clientes = [] #Lista para alamacenar la informacion

while True:
        nombre = (input("Ingrese el nombre del cliente (o escriba fin para terminar): "))
        if nombre == "fin":
            break

        direccion = input("Introduza su direccion: ")
        correo_Electronico = (input("Introduza su correo electronico: "))
        numero_Telefono = int(input("Introduzca su numero telefonico: "))

        #Almacenamos la informacion en una lista (Diccionario)
        clientes.append({"Nombre": nombre, "Dirección": direccion, "Correo electrónico": correo_Electronico, "Número de teléfono": numero_Telefono})

for cliente in clientes:
     print("\nNombre: ", cliente["Nombre"])
     print("\nDireccion: ", cliente["Dirección"])
     print("\nCorreo electronico: ", cliente["Correo electrónico"])
     print("\nNumero de Telefono: ", cliente["Número de teléfono"])