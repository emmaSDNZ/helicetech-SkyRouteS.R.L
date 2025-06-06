from conexion import conectar
from datetime import datetime, timedelta
<<<<<<< HEAD

=======
#menu gestionar ventas
>>>>>>> dev
def gestionar_ventas():
    print ("Usted selecciono la opcion 3)Gestionar Ventas")
#sub menu opcion 3
    while True:
        print("1)Registrar una venta")
        print("2)Volver al Menu Principal ")
        opcion1=input("elija una opcion: ")

        db=conectar()
        cursor=db.cursor()


        if opcion1=="1":
            print("Submenu Gestionar Ventas")
            print("Selecciono la opcion 1)Registrar una venta")
            cliente_id= input ("ID Cliente: ")
            usuario_id=input ("ID usuario: ")
            fecha= datetime.now()
            cursor.execute(
                "INSERT INTO venta (id_cliente, id_usuario, fecha_venta, estado) VALUES (%s,%s,%s,%s)",
                (cliente_id,usuario_id,fecha,"Activa"))
            db.commit()
            print("Venta Registrada")

        elif opcion1=="2":
            print("Submenu Gestionar Ventas")
            print("Selecciono la opcion 2)Volver a menu principal")
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
    db=conectar()
    cursor= db.cursor()
    ahora=datetime.now()
<<<<<<< HEAD
    hace_5_min= ahora- timedelta(minutes=-5)
    cursor.execute("SELECT id_venta FROM anulacion WHERE estado='Activa' AND fecha >= %s", (hace_5_min))
    venta = cursor.fetchone()

    if venta:
        id_venta= venta[0]
        cursor.execute("UPDATE venta SET estado='Anulada', fecha_anulacion=%s WHERE id_venta=%s",
                       (ahora,id_venta))
=======
    hace_5_min= ahora- timedelta(minutes=5)
    cursor.execute("SELECT id_venta FROM venta WHERE estado='Activa' AND fecha_venta >= %s", (hace_5_min,))
    venta = cursor.fetchone()
    

    if venta:
        id_venta= venta[0]
        cursor.execute("UPDATE venta SET estado='Anulada' WHERE id_venta=%s",
                       (id_venta,))
        cursor.execute("UPDATE anulacion SET fecha_anulacion=%s WHERE id_venta=%s",
                       (ahora,id_venta))
        
>>>>>>> dev
        db.commit()
        print ("Venta Anulada")
    else:
        print("No hay ventas recientes")
    cursor.close()
    db.close()
    
