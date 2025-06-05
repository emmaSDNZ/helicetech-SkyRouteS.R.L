def gestionar_ventas():
    print ("Usted selecciono la opcion 3)Gestionar Ventas")
#sub menu opcion 3
    while True:
        print("1)Venta por Cliente")
        print("2)Venta por Destino")
        print("3)Ventas del Mes")
        print("4)Volver al Menu Principal.")
        opcion1=input("elija una opcion: ")
        if opcion1=="1":
            print("Submenu Gestionar Ventas")
            print("Selecciono la opcion 1)Venta por Cliente")
            print("Las ventas por Cliente son:  ")
        elif opcion1=="2":
            print("Submenu Gestionar Ventas")
            print("Selecciono la opcion 2)Ventas por Destino")
            print("Las Ventas por Destino son: ")
        elif opcion1=="3":
            print("Submenu Gestionar Ventas")
            print("Selecciono la opcion 3)Venta del Mes: ")
            print("Las ventas del Mes son: ")
        elif opcion1=="5":
            print("Submenu Gestionar Ventas")
            print("Selecciono la opcion 5)Volver a menu principal")
            print("VOLVIO AL MENU PRINCIPAL")
            break
        else:
            print("OPCION INVALIDA")

def consultar_ventas():
    print ("Usted selecciono la opcion 4) Consultar Ventas")
    print("funcion en proceso: ")
    print("se mostraron Ventas")

def boton_de_arrepentimiento():
    print ("Usted selecciono la opcion 5) Boton de Arrepentimiento")
    print("funcion en proceso ")