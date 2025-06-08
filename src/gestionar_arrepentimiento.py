from datetime import datetime, timedelta
from sql_consultas import (
    obtener_ventas_activas_recientes, 
    anular_venta)

def boton_de_arrepentimiento():
    menu= """
        Usted seleccionó la opción 4) Botón de Arrepentimiento
    """
    print(menu)

    ahora = datetime.now()
    hace_5_min = ahora - timedelta(minutes=5)

    ventas = obtener_ventas_activas_recientes(hace_5_min)

    if len(ventas) == 0:
        print("No hay ventas activas recientes para anular.")
        return

    print("Ventas activas recientes:")
    for v in ventas:
        print(f"ID Venta: {v[0]}, Cliente: {v[1]}, Usuario: {v[2]}, Fecha: {v[3]}")

    id_valido = False
    while not id_valido:
        id_input = input("Ingrese el ID de la venta a anular (o 0 para cancelar): ")
        if not id_input.isdigit():
            print("Por favor, ingrese un número válido.")
            continue

        id_venta = int(id_input)
        if id_venta == 0:
            print("Operación cancelada.")
            break

        # Verificar si el ID ingresado es válido
        encontrado = any(v[0] == id_venta for v in ventas)

        if encontrado:
            try:
                anular_venta(id_venta, ahora)
                print("Venta anulada correctamente.")
            except:
                print("Error al anular la venta.")
            id_valido = True
        else:
            print("ID de venta no válido. Intente nuevamente.")
