import os

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
# Función para vender boletos
def vender_boletos(usuario):
    asientosHora1 = list(range(1, 11))
    asientosHora2 = list(range(1, 11))
    asientosHora3 = list(range(1, 11))
    boletosComprados1 = []
    boletosComprados2 = []
    boletosComprados3 = []
    tarjetas = []
    horario = 0
    opcion = 0
    precio = 2700

    print("Venta de boletos: \n")
    while opcion != 3:
        opcion = int(input("\nEscoja una de las opciones: \n 1. Ver boletos disponibles \n 2. Comprar boletos \n 3. Salir\n"))

        if opcion == 1:
            while horario != 4:
                horario = int(input("\nEscoja un horario: \n1. 2:00pm \n2. 6:30pm \n3. 10:00pm \n4. Volver\n"))
                if horario == 1:
                    print("Asientos disponibles para las 2:00pm:", asientosHora1)
                    break
                elif horario == 2:
                    print("Asientos disponibles para las 6:30pm:", asientosHora2)
                    break
                elif horario == 3:
                    print("Asientos disponibles para las 10:00pm:", asientosHora3)
                    break
                elif horario == 4:
                    break
        if opcion == 2:
            cantidad = 0
            horario = 0
            print("El precio de las entradas es de:", precio)
            while horario != 4:
                horario = int(input("\nEscoja un horario: \n1. 2:00pm \n2. 6:30pm \n3. 10:00pm \n4. Cancelar\n"))
                if horario in [1, 2, 3]:
                    asientos_disponibles = []
                    if horario == 1:
                        asientos_disponibles = asientosHora1
                    elif horario == 2:
                        asientos_disponibles = asientosHora2
                    elif horario == 3:
                        asientos_disponibles = asientosHora3
                    while True:
                        cantidad = int(input("Ingrese la cantidad de boletos a comprar: "))
                        if 0 < cantidad <= len(asientos_disponibles):
                            break
                        else:
                            print("Cantidad de boletos no válida. Intente de nuevo.")
                    for i in range(cantidad):
                        while True:
                            boleto = int(input(f"Ingrese el número del boleto {i + 1}: "))
                            if boleto in asientos_disponibles:
                                boletosComprados = None
                                if horario == 1:
                                    boletosComprados = boletosComprados1
                                elif horario == 2:
                                    boletosComprados = boletosComprados2
                                elif horario == 3:
                                    boletosComprados = boletosComprados3
                                boletosComprados.append(boleto)
                                asientos_disponibles.remove(boleto)
                                break
                            else:
                                print("Número de boleto no válido o ya comprado. Intente de nuevo.")
                    total = precio * cantidad
                    print("Su total es de:", total)
                    tarjeta = int(input("Ingrese el número de su tarjeta de Crédito/Débito: "))
                    confirmacion = int(input("\nDesea confirmar su compra?\n1. SI\n2. NO\n"))
                    if confirmacion == 1:
                        tarjetas.append(tarjeta)
                        print("\n¡Muchas gracias por su compra! ¡Disfrute la película!\n")
                        break
                    elif confirmacion == 2:
                        if horario == 1:
                            asientosHora1 = list(range(1, 11))
                            boletosComprados1 = []
                        elif horario == 2:
                            asientosHora2 = list(range(1, 11))
                            boletosComprados2 = []
                        elif horario == 3:
                            asientosHora3 = list(range(1, 11))
                            boletosComprados3 = []
                        print("\nVenta cancelada. Los asientos han sido liberados.\n")
                        break
            if horario == 4:
                break
# Función para registrar la venta de boletos por usuario
def registrar_venta(usuario, horario, cantidad):
    with open("ventas.txt", "a") as archivo:
        archivo.write(f"{usuario},{horario},{cantidad}\n")
# Menú para agregar, editar, inactivar clientes y vender boletos
while True:
    print("\n1. Agregar cliente")
    print("2. Editar cliente")
    print("3. Inactivar cliente")
    print("4. Mostrar clientes")
    print("5. Vender boletos")
    print("6. Salir")
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
        usuario = input("Ingrese su nombre de usuario: ") 
        vender_boletos(usuario)
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, inténtelo de nuevo.")

