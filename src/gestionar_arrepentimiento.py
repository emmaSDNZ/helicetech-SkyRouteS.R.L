from datetime import datetime, timedelta
from sql_consultas import (
    obtener_ventas_activas_recientes, 
    anular_venta)

def boton_de_arrepentimiento():
    """
    Permite anular ventas activas realizadas en los últimos 5 minutos mediante una interacción por consola.

    Descripción:
    ------------
    Esta función simula un "botón de arrepentimiento" para que el usuario pueda anular
    una venta activa reciente, es decir, realizada en los últimos 5 minutos.
    Muestra las ventas activas recientes, solicita al usuario que ingrese el ID de la venta a anular,
    valida la entrada y realiza la anulación si el ID es correcto.

    Parámetros:
    -----------
    No recibe parámetros.

    Retorna:
    --------
    None

    Flujo:
    ------
    1. Calcula la fecha y hora actuales y la fecha/hora de hace 5 minutos.
    2. Obtiene las ventas activas desde hace 5 minutos usando `obtener_ventas_activas_recientes`.
    3. Si no hay ventas activas recientes, informa y termina la función.
    4. Si hay ventas, las muestra en pantalla con ID, cliente, usuario y fecha.
    5. Solicita al usuario el ID de la venta a anular (o 0 para cancelar).
    6. Valida que el ID sea numérico y corresponda a una venta activa reciente.
    7. Si es válido, llama a `anular_venta` con el ID y fecha actual, e informa resultado.
    8. Si es inválido, solicita reingreso hasta que el usuario cancele o ingrese un ID válido.
    """
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
