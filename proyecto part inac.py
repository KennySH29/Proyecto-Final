# Lista para almacenar la información de los clientes
clientes = [
    {"Nombre": "Ade luz", "Dirección": "Calle Fallas 123", "Correo electrónico": "jdl@example.com", "Número de teléfono": "8775567870", "Activo": True},
    # ... otros clientes
]

def editar_cliente():
    nombre = input("Ingrese el nombre del cliente a editar: ")
    cliente_encontrado = False
    for cliente in clientes:
        if cliente["Nombre"].lower() == nombre.lower():
            cliente_encontrado = True
            print("Editar información del cliente:")
            cliente["Dirección"] = input("Nueva dirección (dejar en blanco para no cambiar): ") or cliente["Dirección"]
            cliente["Correo electrónico"] = input("Nuevo correo electrónico (dejar en blanco para no cambiar): ") or cliente["Correo electrónico"]
            cliente["Número de teléfono"] = input("Nuevo número de teléfono (dejar en blanco para no cambiar): ") or cliente["Número de teléfono"]
            print("Información actualizada con éxito.")
            break
    if not cliente_encontrado:
        print("Cliente no encontrado.")

def inactivar_cliente():
    nombre = input("Ingrese el nombre del cliente a inactivar: ")
    cliente_encontrado = False
    for cliente in clientes:
        if cliente["Nombre"].lower() == nombre.lower():
            cliente_encontrado = True
            cliente["Activo"] = False
            print("Cliente inactivado con éxito.")
            break
    if not cliente_encontrado:
        print("Cliente no encontrado.")

# Menú para editar o inactivar clientes
while True:
    print("\n1. Editar cliente")
    print("2. Inactivar cliente")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        editar_cliente()
    elif opcion == "2":
        inactivar_cliente()
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, inténtelo de nuevo.")


