# Función para agregar un nuevo cliente al archivo
def agregar_cliente(nombre, direccion, correo, telefono):
    with open("clientes.txt", "a") as archivo:
        archivo.write(f"{nombre},{direccion},{correo},{telefono},activo\n")

# Función para mostrar todos los clientes almacenados en el archivo
def mostrar_clientes():
    with open("clientes.txt", "r") as archivo:
        for linea in archivo:
            cliente_info = linea.strip().split(",")
            nombre, direccion, correo, telefono = cliente_info[:4]
            activo = cliente_info[4] if len(cliente_info) == 5 else "activo"
            estado = "Activo" if activo == "activo" else "Inactivo"
            print("Nombre:", nombre)
            print("Dirección:", direccion)
            print("Correo electrónico:", correo)
            print("Número de teléfono:", telefono)
            print("Estado:", estado)
            print()

# Función para editar la información de un cliente
def editar_cliente(nombre):
    clientes_actualizados = []
    with open("clientes.txt", "r") as archivo:
        for linea in archivo:
            cliente_info = linea.strip().split(",")
            if cliente_info[0] == nombre:
                direccion = input("Nueva dirección (dejar en blanco para no cambiar): ") or cliente_info[1]
                correo = input("Nuevo correo electrónico (dejar en blanco para no cambiar): ") or cliente_info[2]
                telefono = input("Nuevo número de teléfono (dejar en blanco para no cambiar): ") or cliente_info[3]
                activo = cliente_info[4] if len(cliente_info) == 5 else "activo"
                cliente_info = [nombre, direccion, correo, telefono, activo]
            clientes_actualizados.append(cliente_info)
    with open("clientes.txt", "w") as archivo:
        for cliente_info in clientes_actualizados:
            archivo.write(",".join(cliente_info) + "\n")
    print("Cliente actualizado con éxito.")

# Función para inactivar un cliente
def inactivar_cliente(nombre):
    clientes_actualizados = []
    with open("clientes.txt", "r") as archivo:
        for linea in archivo:
            cliente_info = linea.strip().split(",")
            if cliente_info[0] == nombre:
                cliente_info[-1] = "inactivo"
            clientes_actualizados.append(cliente_info)
    with open("clientes.txt", "w") as archivo:
        for cliente_info in clientes_actualizados:
            archivo.write(",".join(cliente_info) + "\n")
    print("Cliente inactivado con éxito.")
# Sistema de seguridad de acceso
usuario = ""
clave = ""

while usuario != "admin" or clave != "123":
    usuario = input("Introduzca su usuario: ")
    clave = input("Introduzca su clave: ")
    if usuario == "admin" and clave == "123":
        print("¡Bienvenido!")
    else:
        print("Acceso denegado, inténtelo otra vez")

# Menú para agregar, editar o inactivar clientes
while True:
    print("\n1. Agregar cliente")
    print("2. Editar cliente")
    print("3. Inactivar cliente")
    print("4. Mostrar clientes")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        direccion = input("Introduzca su dirección: ")
        correo = input("Introduzca su correo electrónico: ")
        telefono = input("Introduzca su número de teléfono: ")
        agregar_cliente(nombre, direccion, correo, telefono)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del cliente a editar: ")
        editar_cliente(nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del cliente a inactivar: ")
        inactivar_cliente(nombre)
    elif opcion == "4":
        print("\nListado de clientes:")
        mostrar_clientes()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, inténtelo de nuevo.")
