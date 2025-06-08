import os

def sql_ejecutar(conexion):
    # Obtengo el directorio donde está este archivo
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_sql = os.path.join(dir_actual, '..', 'data', 'helice_bd.sql')

    with open(ruta_sql, 'r', encoding='utf-8') as f:
        script = f.read()

    cursor = conexion.cursor()
    sentencias = script.split(';')
    for sentencia in sentencias:
        sentencia = sentencia.strip()
        if sentencia:
            cursor.execute(sentencia)
            while cursor.nextset():
                pass
    conexion.commit()
    cursor.close()