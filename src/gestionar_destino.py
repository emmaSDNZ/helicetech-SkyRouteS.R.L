from conexion import conectar

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

        db= conectar()
        cursor= db.cursor()

        if opcion1=="1":
            cursor.execute("SELEC * FROM destino")
            destino= cursor.fetchall()
            print("Submenu Gestionar Destinos")
            print("Selecciono la opcion 1)Ver Destinos")
            print("El listado de Destinos es  ")
            for d in destino:
                print(f"{d[0]} - {d[1]}, {d[2]} (${d[3]})")

        elif opcion1=="2":
            print("Submenu Gestionar Destinos")
            print("Selecciono la opcion 2)Agregar Destinos")
            print("Ingresar los siguientes datos para agregar Destinos ")
            ciudad=input("Ciudad: ")
            pais=input("Pais: ")
            costo=float(input("Costo base: "))
            cursor.execute("INSERT INTO destino (ciudad, pais, costo_base) VALUES (%s,%s,%s)",
            (ciudad,pais,costo))
            db.commit()
            print("Destino Agregado")


        elif opcion1=="3":
            print("Submenu Gestionar Destinos")
            print("Selecciono la opcion 3)Modificar Destinos: ")
            id_destino=input("ID del destino a modificar: ")
            ciudad=input("Nueva ciudad: ")
            pais=input("Nuevo Pais: ")
            costo=float(input("Nuevo Costo base: "))
            cursor.execute("UPDATE destino SET ciudad=%s, pais=%s, costo_base=%s WHERE id_destino=%s",
                           (ciudad,pais,costo,id_destino))
            db.commit()
            print ("Destino Modificado")

        elif opcion1=="4":
            print("Submenu Gestionar Destinos")
            print("Selecciono la opcion 4)Eleminar Destinos: ")
            id_destino=input("ID destino a eleminar: ")
            cursor.execute("DELETE FROM destino WHERE  id_destino=%s", (id_destino))
            db.commit()
            print("Destino Eleminado")
        
        elif opcion1=="5":
            print("Submenu Gestionar Destinos")
            print("Selecciono la opcion 5)Volver a menu principal")
            print("VOLVIO AL MENU PRINCIPAL")
            break
        else:
            print("OPCION INVALIDA")
        cursor.close()
        db.close()
        