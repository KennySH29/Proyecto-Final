import os
import random

#Agregar un nuevo cliente al archivo
def agregar_cliente(nombre, direccion, correo, telefono):
    with open("clientes.txt", "a") as archivo:
        archivo.write(f"{nombre},{direccion},{correo},{telefono},activo\n")

# Mostrar todos los clientes
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

# Editar la información de un cliente
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

# Inactivar un cliente
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

# Vender boletos
def vender_boletos(usuario):
   
    asientosHora1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    asientosHora2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    asientosHora3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    boletosComprados1 = []
    boletosComprados2 = []
    boletosComprados3 = []
    tarjetas = []
    opcion = 0
    precio = 2700

    print("Venta de boletos: \n")
    while opcion != 3:
        opcion = int(input("\nEscoja una de las opciones: \n 1. Ver boletos disponibles \n 2. Comprar boletos \n 3. Salir\n"))

        if opcion == 1:
            print("Horarios disponibles:")
            print("1. 2:00pm")
            print("2. 6:30pm")
            print("3. 10:00pm")
            print("4. Cancelar")
            horario = int(input("\nEscoja un horario: "))
            if horario in [1, 2, 3]:
                asientos_disponibles = []
                if horario == 1:
                    asientos_disponibles = asientosHora1
                elif horario == 2:
                    asientos_disponibles = asientosHora2
                elif horario == 3:
                    asientos_disponibles = asientosHora3
                print("Asientos disponibles:", asientos_disponibles)

        elif opcion == 2:
            horario = int(input("\nEscoja un horario: "))
            if horario in [1, 2, 3]:
                asientos_disponibles = []
                if horario == 1:
                    asientos_disponibles = asientosHora1
                elif horario == 2:
                    asientos_disponibles = asientosHora2
                elif horario == 3:
                    asientos_disponibles = asientosHora3

                cantidad = int(input("Ingrese la cantidad de boletos a comprar: "))
                if 0 < cantidad <= len(asientos_disponibles):
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
                    impuestos = total * 0.13
                    total_con_impuestos = total + impuestos

                    # Número de transacción Aleatorio
                    numero_transaccion = str(random.randint(1, 999999))
                    # Guardar información de la venta 
                    with open("ventas.txt", "a") as archivo:
                        archivo.write(f"{usuario},{horario},{cantidad},{total},{impuestos},{total_con_impuestos},{numero_transaccion}\n")
                    print("Su total es de:", total)
                    print("Impuestos:", impuestos)
                    print("Total con impuestos:", total_con_impuestos)
                    print("Número de transacción:", numero_transaccion)
                    tarjeta = int(input("Ingrese el número de su tarjeta de Crédito/Débito: "))
                    confirmacion = int(input("\nDesea confirmar su compra?\n1. SI\n2. NO\n"))
                    if confirmacion == 1:
                        tarjetas.append(tarjeta)
                        print("\n¡Muchas gracias por su compra! ¡Disfrute la película!\n")
                        break
                    elif confirmacion == 2:
                        # Agregar los boletos cancelados de vuelta a la lista de asientos disponibles
                        asientos_disponibles.extend(boletosComprados)
                        print("\nVenta cancelada. Los asientos han sido liberados.\n")
                        break
        elif opcion == 3:
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
# Mostrar el historial de ventas
def mostrar_historial_ventas():
    print("Historial de ventas:\n")
    with open("ventas.txt", "r") as archivo_ventas:
        for linea in archivo_ventas:
            print(linea.strip())
        else:
            print("No hay ventas registradas.")

def anular_factura(numero_transaccion):
    with open("ventas.txt", "r") as archivo_ventas:
        lineas = archivo_ventas.readlines()
    factura_encontrada = False
    with open("ventas.txt", "w") as archivo_ventas:
        for linea in lineas:
            if str(numero_transaccion) in linea:
                factura_encontrada = True
                print("Factura anulada con éxito.")
            else:        
                archivo_ventas.write(linea)
    if not factura_encontrada:
        print("No se encontró ninguna factura con ese número de transacción.")
# Menú principal
while True:
    print("\n1. Agregar cliente")
    print("2. Editar cliente")
    print("3. Inactivar cliente")
    print("4. Mostrar clientes")
    print("5. Vender boletos")
    print("6. Anular factura")
    print("7. Mostrar historial de ventas")
    print("8. Salir")
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
        numero_transaccion = input("Ingrese el número de transacción de la factura a anular: ")
        anular_factura(numero_transaccion)
    elif opcion == "7":
        print("\nHistorial de ventas:")
        mostrar_historial_ventas()
    elif opcion == "8":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, inténtelo de nuevo.")
