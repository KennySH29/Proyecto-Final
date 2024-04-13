#Adrian Guido Rojas, Glenda Rodriguez Morales, Dylan Sanabria Fernández, Melvin Rojas Hernandez, Kenny Salazar Herrera
    #GRUPO 8
def agregar_cliente(nombre, direccion, correo, telefono):
    with open("clientes.txt", "a") as archivo:
        archivo.write(f"{nombre},{direccion},{correo},{telefono}\n")

# Función para mostrar todos los clientes almacenados en el archivo
def mostrar_clientes():
    with open("clientes.txt", "r") as archivo:
        for linea in archivo:
            nombre, direccion, correo, telefono = linea.strip().split(",")
            print("Nombre:", nombre)
            print("Dirección:", direccion)
            print("Correo electrónico:", correo)
            print("Número de teléfono:", telefono)
            print()

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



while True:
        nombre = (input("Ingrese el nombre del cliente (o escriba fin para terminar): "))
        if nombre == "fin":
            break

        direccion = input("Introduza su direccion: ")
        correo_Electronico = (input("Introduza su correo electronico: "))
        numero_Telefono = int(input("Introduzca su numero telefonico: "))


        agregar_cliente(nombre, direccion, correo_Electronico, numero_Telefono)

# Mostrar todos los clientes almacenados
print("\nListado de clientes:")
mostrar_clientes()

  
