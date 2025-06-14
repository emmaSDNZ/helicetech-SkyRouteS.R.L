from datetime import datetime, timedelta
#menu gestionar ventas
from conexion import conectar
from sql_consultas import select_all_from, insert_into, select_where
from datetime import datetime

def gestionar_ventas():
    """
    Función interactiva para gestionar ventas desde un menú por consola.

    Descripción:
    ------------
    Permite al usuario registrar nuevas ventas asociadas a clientes y usuarios,
    visualizar el listado de ventas registradas, o volver al menú principal.
    Utiliza funciones SQL para consultar y modificar la base de datos.

    Operaciones:
    ------------
    1) Registrar una venta:
       - Muestra lista de clientes y usuarios disponibles.
       - Solicita IDs para cliente y usuario.
       - Valida que existan en la base.
       - Registra la venta con la fecha actual y estado 'Activa'.

    2) Ver ventas registradas:
       - Muestra listado completo de ventas con sus datos principales.

    3) Volver al menú principal:
       - Sale del submenú.

    Parámetros:
    -----------
    No recibe parámetros.

    Retorna:
    --------
    None

    Flujo:
    ------
    - Muestra el submenú y pide opción al usuario.
    - Ejecuta la operación según la opción.
    - Valida la existencia de cliente y usuario al registrar ventas.
    - Permite salir del submenú con la opción 3.
    """
    print("Usted seleccionó la opción 3) Gestionar Ventas")

    while True:
        menu = """
        Submenu Gestionar Ventas
        1) Registrar una venta
        2) Ver ventas registradas
        3) Volver al menú principal
        """
        print(menu)
        opcion1 = input("Elija una opción: ")

        if opcion1 == "1":
            print("Submenu Gestionar Ventas")
            print("Seleccionó la opción 1) Registrar una venta")

            # Ver lista de clientes
            print("Listado de clientes disponibles:")
            clientes = select_all_from("cliente")
            for c in clientes:
                print(f"ID: {c[0]}, Nombre: {c[1]}, Apellido: {c[2]}")

            cliente_id = input("Ingrese el ID del cliente: ")
            cliente_existente = select_where("cliente", "id_cliente", cliente_id)
            if not cliente_existente:
                print(f"No existe cliente con ID {cliente_id}")
                continue

            # Ver lista de usuarios
            print("Listado de usuarios disponibles:")
            usuarios = select_all_from("usuario")
            for u in usuarios:
                print(f"ID: {u[0]}, Nombre de usuario: {u[1]}")

            usuario_id = input("Ingrese el ID del usuario: ")
            usuario_existente = select_where("usuario", "id_usuario", usuario_id)
            if not usuario_existente:
                print(f"No existe usuario con ID {usuario_id}")
                continue

            # Registrar la venta
            fecha = datetime.now()
            insert_into(
                "venta",
                ["id_cliente", "id_usuario", "fecha_venta", "estado"],
                (cliente_id, usuario_id, fecha, "Activa")
            )
            print("Venta registrada correctamente.")

        elif opcion1 == "2":
            print("Submenu Gestionar Ventas")
            print("Seleccionó la opción 2) Ver ventas registradas")
            ventas = select_all_from("venta")
            print("Listado de ventas:")
            for v in ventas:
                print(f"ID Venta: {v[0]}, Cliente ID: {v[1]}, Usuario ID: {v[2]}, Fecha: {v[3]}, Estado: {v[4]}")

        elif opcion1 == "3":
            print("Submenu Gestionar Ventas")
            print("Seleccionó la opción 3) Volver al menú principal")
            print("VOLVIÓ AL MENÚ PRINCIPAL")
            break

        else:
            print("OPCIÓN INVÁLIDA")

