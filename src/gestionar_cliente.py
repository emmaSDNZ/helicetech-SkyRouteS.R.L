def gestionar_cliente():
    print ("Usted selecciono la opcion 1)Gestionar Clientes.")
#sub menu opcion 1
    while True:
        print("Submenu Gestionar Cliente")
        print("1)Ver Cliente")
        print("2)Agregar Cliente")
        print("3)Modificar Cliente")
        print("4)Eliminar Cliente")
        print("5)Volver a menu principal")
        opcion1=input("Elija una opcion: ")
        if opcion1=="1":
            print("Submenu Gestionar Cliente")
            print("Selecciono la opcion 1)Ver Cliente")
            print("El listado de cliente es  ")
        elif opcion1=="2":
            print("Submenu Gestionar Cliente")
            print("Selecciono la opcion 2)Agregar Cliente")
            print("Ingresar los siguientes datos para agregar cliente ")
            nombre_cliente=input("Ingrese el nombre: ")
            apellido_cliente=input("Ingrese el apellido: ")
            dni_cliente=input("Ingrese el DNI: ")
            print(f"Cliente agregado: {nombre_cliente} {apellido_cliente} {dni_cliente}")
        elif opcion1=="3":
            print("Submenu Gestionar Cliente")
            print("Selecciono la opcion 3)Modificar Cliente: ")
        elif opcion1=="4":
            print("Submenu Gestionar Cliente")
            print("Selecciono la opcion 4)Eleminar cliente: ")
        elif opcion1=="5":
            print("Submenu Gestionar Cliente")
            print("Selecciono la opcion 5)Volver a menu principal")
            print("VOLVIO AL MENU PRINCIPAL")
            break
        else:
            print("OPCION INVALIDA")
            