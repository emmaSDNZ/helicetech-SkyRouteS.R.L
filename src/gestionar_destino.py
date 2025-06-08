
from sql_consultas import (
    select_all_from, 
    insert_into, 
    update_table, 
    select_where, 
    delete_from)

# Menu Gestionar Destinos
def gestionar_destino():
    print("Usted seleccionó la opción 2) Gestionar Destinos")

    while True:
        # Sub menú opción 2
        menu = """
            Submenu Gestionar Destinos
            1) Ver Destinos
            2) Agregar Destinos
            3) Modificar Destinos
            4) Eliminar Destino
            ) Volver al menú principal"
                """
        print(menu)
        opcion1 = input("Elija una opción: ")

        if opcion1 == "1":
            print("Submenu Gestionar Destinos")
            print("Seleccionó la opción 1) Ver Destinos")
            print("El listado de destinos es:")
            destinos = select_all_from("destino")
            for d in destinos:
                print(f"{d[0]} - {d[1]}, {d[2]} (${d[3]})")

        elif opcion1 == "2":
            print("Submenu Gestionar Destinos")
            print("Seleccionó la opción 2) Agregar Destinos")
            print("Ingresar los siguientes datos para agregar destino")
            ciudad = input("Ciudad: ")
            pais = input("País: ")
            costo = float(input("Costo base: "))

            insert_into(
                "destino",
                ["ciudad", "pais", "costo_base"],
                (ciudad, pais, costo)
            )
            print("Destino agregado correctamente.")

        elif opcion1 == "3":
            print("Submenu Gestionar Destinos")
            print("Seleccionó la opción 3) Modificar Destinos")
            id_destino = input("ID del destino a modificar: ")

            # Validar si existe el destino antes de modificar
            destino_existente = select_where("destino", "id_destino", id_destino)
            if not destino_existente:
                print(f"No existe destino con ID {id_destino}")
            else:
                ciudad = input("Nueva ciudad: ")
                pais = input("Nuevo país: ")
                costo = float(input("Nuevo costo base: "))

                update_table(
                    "destino",
                    ["ciudad", "pais", "costo_base"],
                    (ciudad, pais, costo),
                    "id_destino",
                    id_destino
                )
                print("Destino modificado correctamente.")

        elif opcion1 == "4":
            print("Submenu Gestionar Destinos")
            print("Seleccionó la opción 4) Eliminar Destinos")
            id_destino = input("ID del destino a eliminar: ")

            # Validar si existe el destino antes de eliminar
            destino_existente = select_where("destino", "id_destino", id_destino)
            if not destino_existente:
                print(f"No existe destino con ID {id_destino}")
            else:
                delete_from("destino", "id_destino", id_destino)
                print("Destino eliminado correctamente.")

        elif opcion1 == "5":
            print("Submenu Gestionar Destinos")
            print("Seleccionó la opción 5) Volver al menú principal")
            print("VOLVIÓ AL MENÚ PRINCIPAL")
            break

        else:
            print("OPCIÓN INVÁLIDA")
