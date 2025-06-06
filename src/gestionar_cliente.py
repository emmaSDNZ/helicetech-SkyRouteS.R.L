from conexion import conectar

<<<<<<< HEAD

=======
#menu de gestionar clientes
>>>>>>> dev
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

        db=conectar()
        cursor= db.cursor()

        if opcion1=="1":
            cursor.execute("SELECT * FROM cliente")
            clientes= cursor.fetchall()
            print("Submenu Gestionar Cliente")
            print("Selecciono la opcion 1)Ver Cliente")
            print("El listado de cliente es  ")
            for cli in clientes:
                print(f"{cli[0]} - {cli[1]} {cli[2]} (DNI: {cli[3]}")
                      
        elif opcion1=="2":
            print("Submenu Gestionar Cliente")
            print("Selecciono la opcion 2)Agregar Cliente")
            print("Ingresar los siguientes datos para agregar cliente ")
            razon_social=input("Ingrese el razon social: ")
            cuit=input("Ingrese el cuit: ")
            correo=input("Ingrese el correo: ")
            cursor.execute("INSERT INTO cliente (razon_social,cuit,correo) VALUES (%s,%s,%s)",
                           (razon_social,cuit,correo))
            db.commit()
            print("cliente agregado")

        elif opcion1=="3":
            print("Submenu Gestionar Cliente")
            print("Selecciono la opcion 3)Modificar Cliente")
            id_cliente = input("Ingrese el ID del cliente a modificar: ")
            nueva_razon = input("Nueva razon social: ")
            nuevo_cuit = input("Nuevo cuit: ")
            nuevo_correo = input("Nuevo correo: ")
<<<<<<< HEAD
            cursor.execute("UPDATE cliente SET razon_social=%s, cuit=%s, correo=%s WHERE id=%s",
                           (nueva_razon, nuevo_cuit, nuevo_correo, id_cliente))
=======
            cursor.execute("UPDATE cliente SET razon_social=%s, cuit=%s, correo=%s WHERE id_cliente=%s",
                           (nueva_razon, nuevo_cuit, nuevo_correo, id_cliente))
            db.commit()
>>>>>>> dev
            print ("cliente modificado")
        elif opcion1=="4":
            print("Submenu Gestionar Cliente")
            print("Selecciono la opcion 4)Eleminar cliente: ")
            id_cliente=input("Ingrese el ID del cliente a eleminar: ")
<<<<<<< HEAD
            cursor.execute("DELETE FROM cliente WHERE id=%s", (id_cliente))
            db.commit
=======
            cursor.execute("DELETE FROM cliente WHERE id_cliente=%s", (id_cliente,))
            db.commit()
>>>>>>> dev
            print ("cliente eleminado ")

        elif opcion1=="5":
            print("Submenu Gestionar Cliente")
            print("Selecciono la opcion 5)Volver a menu principal")
            print("VOLVIO AL MENU PRINCIPAL")
            break
        else:
            print("OPCION INVALIDA")
        cursor.close()
        db.close()
            