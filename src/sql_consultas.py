from conexion import conectar
import mysql.connector
from mysql.connector import IntegrityError
db = conectar()
cursor = db.cursor()

def select_all_from(nombre_tabla):
    """
    Realiza una consulta SELECT * sobre la tabla especificada y devuelve todos los registros.

    Parámetros:
    ----------
    nombre_tabla : str
        Nombre de la tabla de la cual se desea obtener todos los registros.

    Retorna:
    -------
    Lista de tuplas con todas las filas obtenidas de la tabla.
    """
    # IMPORTANTE: Aquí asumimos que nombre_tabla es seguro y controlado.
    query = f"SELECT * FROM {nombre_tabla}"
    cursor.execute(query)
    return cursor.fetchall()

def insert_into(nombre_tabla, columnas, valores):
    """
    Inserta un registro en la tabla especificada.

    Parámetros:
    ----------
    nombre_tabla : str
        Nombre de la tabla donde se insertará el registro.
    columnas : list of str
        Nombres de las columnas donde insertar valores.
    valores : list o tuple
        Valores a insertar, en el mismo orden que columnas.

    Retorna:
    -------
    None
    """
    signos_pregunta = ", ".join(["%s"] * len(valores))
    columnas_str = ", ".join(columnas)
    query = f"INSERT INTO {nombre_tabla} ({columnas_str}) VALUES ({signos_pregunta})"
    cursor.execute(query, valores)
    db.commit()

def update_table(nombre_tabla, columnas, valores, condicion_col, condicion_valor):
    """
    Actualiza registros en una tabla según una condición.

    Parámetros:
    -----------
    nombre_tabla : str
        Tabla a actualizar.
    columnas : list de str
        Columnas a actualizar.
    valores : list o tuple
        Nuevos valores correspondientes a las columnas.
    condicion_col : str
        Columna para condición WHERE.
    condicion_valor : any
        Valor para condición WHERE.

    Retorna:
    --------
    None
    """
    set_clause = ", ".join([f"{col}=%s" for col in columnas])
    query = f"UPDATE {nombre_tabla} SET {set_clause} WHERE {condicion_col}=%s"
    parametros = list(valores) + [condicion_valor]
    cursor.execute(query, parametros)
    db.commit()

def select_where(nombre_tabla, condicion_columna, valor):
    """
    Realiza SELECT * WHERE condicion_columna = valor.

    Parámetros:
    -----------
    nombre_tabla : str
        Tabla donde se hace la consulta.
    condicion_columna : str
        Columna para condición WHERE.
    valor : any
        Valor para condición.

    Retorna:
    --------
    Lista de tuplas con resultados.
    """
    query = f"SELECT * FROM {nombre_tabla} WHERE {condicion_columna} = %s"
    cursor.execute(query, (valor,))
    return cursor.fetchall()

def delete_from(nombre_tabla, condicion_col, condicion_valor):
    """
    Elimina registros de una tabla según condición.

    Parámetros:
    -----------
    nombre_tabla : str
        Tabla donde eliminar registros.
    condicion_col : str
        Columna para condición WHERE.
    condicion_valor : any
        Valor que identifica qué eliminar.

    Retorna:
    --------
    None
    """
    query = f"DELETE FROM {nombre_tabla} WHERE {condicion_col}=%s"
    try:
        cursor.execute(query, (condicion_valor,))
        db.commit()
    except mysql.connector.IntegrityError as e:
        if e.errno == 1451:
            print(f"No se puede eliminar el registro de {nombre_tabla} porque tiene datos asociados.")
        else:
            print(f"Error inesperado al eliminar en {nombre_tabla}: {e}")
            raise



def obtener_ventas_activas_recientes(desde_fecha):
    """
    Devuelve las ventas activas realizadas desde 'desde_fecha' hasta ahora.

    Parámetros:
    -----------
    desde_fecha : datetime
        Fecha desde la cual buscar ventas activas.

    Retorna:
    --------
    Lista de tuplas con las ventas activas recientes.
    """
    query = """
    SELECT id_venta, id_cliente, id_usuario, fecha_venta 
    FROM venta 
    WHERE estado='Activa' AND fecha_venta >= %s 
    ORDER BY fecha_venta DESC
    """
    cursor.execute(query, (desde_fecha,))
    return cursor.fetchall()

def anular_venta(id_venta, fecha_anulacion):
    """
    Anula una venta y actualiza su registro de anulación.

    Parámetros:
    -----------
    id_venta : int
        ID de la venta a anular.
    fecha_anulacion : datetime
        Fecha de anulación a registrar.

    Retorna:
    --------
    None
    """
    cursor.execute("UPDATE venta SET estado='Anulada' WHERE id_venta=%s", (id_venta,))
    cursor.execute("UPDATE anulacion SET fecha_anulacion=%s WHERE id_venta=%s", (fecha_anulacion, id_venta))
    db.commit()