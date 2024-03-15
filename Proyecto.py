

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

<<<<<<< Updated upstream

#Sistema informacion clientes
clientes = int(input("Ingesar el numero de clientes: "))

for i in range(clientes):
    nombre = input("Ingresar nombre del cliente:")
    correo = input("Ingresar correo electronico:")
    direccion = input("Ingresar direccion:")
    telefono = int(input("Numero de telefono:"))

    nombre.append(nombre)
    correos.append(correo)
    direcciones.append(direccion)
    telefonos.append(telefono)
for i in range(clientes):
    print(f"--NOMBRE: {nombres[i]}")
    print(f"      --Correo: {correos[i]}  --Direccion: {direcciones[i]}/ Telefono: {telefonos[i]}")
