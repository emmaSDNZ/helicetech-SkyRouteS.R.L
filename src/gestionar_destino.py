def gestionar_destino():
    print ("Usted selecciono la opcion 2)Gestionar Destinos")
    while True:
#sub menu opcion 2
        print("Submenu Gestionar Destinos")
        print("1)Ver Destinos")
        print("2)Agregar Destinos")
        print("3)Modificar Destinos")
        print("4)Eliminar Destinos")
        print("5)Volver a menu principal")
        opcion1=input("Elija una opcion: ")
        if opcion1=="1":
            print("Submenu Gestionar Destinos")
            print("Selecciono la opcion 1)Ver Destinos")
            print("El listado de Destinos es  ")
        elif opcion1=="2":
            print("Submenu Gestionar Destinos")
            print("Selecciono la opcion 2)Agregar Destinos")
            print("Ingresar los siguientes datos para agregar Destinos ")
        elif opcion1=="3":
            print("Submenu Gestionar Destinos")
            print("Selecciono la opcion 3)Modificar Destinos: ")
        elif opcion1=="4":
            print("Submenu Gestionar Destinos")
            print("Selecciono la opcion 4)Eleminar Destinos: ")
        elif opcion1=="5":
            print("Submenu Gestionar Destinos")
            print("Selecciono la opcion 5)Volver a menu principal")
            print("VOLVIO AL MENU PRINCIPAL")
            break
        else:
            print("OPCION INVALIDA")