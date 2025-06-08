import os

def sql_ejecutar(conexion):
    """
    Ejecuta un script SQL desde un archivo para inicializar o actualizar
    la base de datos utilizando la conexión proporcionada.

    Parámetros:
    -----------
    conexion : objeto de conexión a la base de datos
        Conexión activa a la base de datos sobre la cual se ejecutará el script.

    Funcionamiento:
    ---------------
    - Obtiene la ruta absoluta del archivo SQL 'helice_bd.sql' ubicado en
      el directorio '../data/' relativo al archivo actual.
    - Lee todo el contenido del archivo SQL.
    - Divide el script en sentencias separadas por ';'.
    - Ejecuta cada sentencia SQL secuencialmente.
    - Limpia el cursor después de cada ejecución para evitar problemas
      con múltiples resultados.
    - Finalmente realiza commit para guardar los cambios en la base de datos.
    - Cierra el cursor.

    Uso:
    ----
    Se debe pasar una conexión válida a la base de datos. Si la conexión no
    está activa o el archivo no existe, la función lanzará una excepción.
    """
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