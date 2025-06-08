def sql_ejecutar(conexion):
    ruta_sql = '../data/helice_bd.sql'  # ruta relativa sin usar os
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