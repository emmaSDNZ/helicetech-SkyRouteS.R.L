from sql_consultas import (
    select_all_from,
    insert_into,
    update_table,
    select_where,
    delete_from
)
#menu de gestionar clientes
def gestionar_cliente():
    """
    Función interactiva para gestionar clientes desde un menú por consola.

    Descripción:
    ------------
    Permite al usuario realizar operaciones básicas de gestión sobre la tabla 'cliente',
    incluyendo ver, agregar, modificar y eliminar clientes.
    Presenta un submenú con opciones que se repite hasta que el usuario elige salir.

    Operaciones:
    ------------
    1) Ver Cliente: Muestra una lista con todos los clientes registrados.
    2) Agregar Cliente: Solicita datos para agregar un nuevo cliente a la base.
    3) Modificar Cliente: Permite modificar los datos de un cliente existente, identificado por su ID.
    4) Eliminar Cliente: Elimina un cliente existente por su ID.
    5) Volver a menú principal: Sale del submenú y retorna al menú principal.

    Parámetros:
    -----------
    No recibe parámetros.

    Retorna:
    --------
    None

    Flujo:
    ------
    - Muestra el submenú y pide una opción.
    - Según la opción:
        - Llama a funciones SQL para obtener, insertar, actualizar o eliminar datos en la tabla 'cliente'.
        - Maneja validaciones simples para verificar existencia del cliente antes de modificar o eliminar.
    - El menú se repite hasta que el usuario elige salir (opción 5).
    """
    
    print ("Usted selecciono la opcion 1)Gestionar Clientes.")

    while True:
        menu = """
        Submenu Gestionar Cliente
        1) Ver Cliente
        2) Agregar Cliente
        3) Modificar Cliente
        4) Eliminar Cliente
        5) Volver a menu principal
        """
        print(menu)  
        opcion1 = input("Elija una opcion: ")

        if opcion1=="1":
            clientes = select_all_from("cliente")
            print("""
            Submenu Gestionar Cliente
            Selecciono la opcion 1) Ver Cliente
            El listado de cliente es:
            """)
            for cli in clientes:
                print(f"{cli[0]} - {cli[1]} {cli[2]} - DNI: {cli[3]}")
                      
        elif opcion1 == "2":
            print("""
            Submenu Gestionar Cliente
            Seleccionó la opción 2) Agregar Cliente
            Ingresar los siguientes datos para agregar cliente
            """)
            razon_social = input("Ingrese el razon social: ")
            cuit = input("Ingrese el cuit: ")
            correo = input("Ingrese el correo: ")
            columnas = ["razon_social", "cuit", "correo"]
            valores = (razon_social, cuit, correo)

            insert_into("cliente", columnas, valores)
            print("Cliente agregado")   

        elif opcion1 == "3":
            print("""
            Submenu Gestionar Cliente
            Selecciono la opcion 3)Modificar Cliente
            """)

            id_cliente = input("Ingrese el ID del cliente a modificar: ")
            cliente_existente = select_where("cliente", "id_cliente", id_cliente)

            if not cliente_existente:
                print(f"No existe cliente con ID {id_cliente}")
            else:
                nueva_razon = input("Nueva razon social: ")
                nuevo_cuit = input("Nuevo cuit: ")
                nuevo_correo = input("Nuevo correo: ")
                columnas = ["razon_social", "cuit", "correo"]
                valores = (nueva_razon, nuevo_cuit, nuevo_correo)

                update_table("cliente", columnas, valores, "id_cliente", id_cliente)
                print("Cliente modificado correctamente")

        elif opcion1 == "4":
            print("""
            Submenu Gestionar Cliente
            Seleccionó la opción 4) Eliminar clien  """)
            id_cliente = input("Ingrese el ID del cliente a eliminar: ")
            cliente = select_where("cliente", "id_cliente", id_cliente)
            if not cliente:
                print(f"No existe cliente con ID {id_cliente}")
            else:
                delete_from("cliente", "id_cliente", id_cliente)
                print("Cliente eliminado correctamente")

        elif opcion1=="5":
            print("Submenu Gestionar Cliente")
            print("Selecciono la opcion 5)Volver a menu principal")
            print("VOLVIO AL MENU PRINCIPAL")
            break
        else:
            print("OPCION INVALIDA")
