import os
import mysql.connector
from mysql.connector import Error

def ejecutar_script_sql(ruta_archivo_sql, conexion):
    """
    Ejecuta un script SQL desde un archivo sobre una conexión MySQL.

    Parámetros:
        ruta_archivo_sql (str): Ruta al archivo .sql que contiene el script.
        conexion (mysql.connector.connection_cext.CMySQLConnection): Conexión MySQL abierta.

    Lanza:
        FileNotFoundError: Si no se encuentra el archivo SQL.
        mysql.connector.Error: Si ocurre un problema durante la ejecución de las sentencias SQL.
    """
    with open(ruta_archivo_sql, "r", encoding="utf-8") as archivo_sql:
        script_sql = archivo_sql.read()
    
    cursor = conexion.cursor()
    # Dividir en sentencias separadas por ";"
    sentencias = script_sql.split(';')
    for sentencia in sentencias:
        sentencia = sentencia.strip()
        if sentencia:  # si no es vacía
            cursor.execute(sentencia)
            # Limpiar resultados si corresponde (previene "Unread result found")
            while cursor.nextset():
                pass
    conexion.commit()

def main():
    """
    Programa principal que:
    - Solicita la contraseña para la base de datos.
    - Ejecuta el script SQL para crear la base y tablas si no existen.
    - Se conecta a la base de datos 'helice'.
    - Verifica la conexión y muestra la base seleccionada.
    - Cierra la conexión al finalizar.
    """
    passwordDB = input("Favor de ingresar PASSWORD para la base de datos: ")

    # Configuración inicial sin especificar base para crear la BD
    db_config_sin_db = {
        "host": "localhost",
        "user": "root",
        "password": passwordDB,
        "port": "3306"
    }

    try:
        # Construir ruta absoluta del archivo SQL relativo al script actual
        ruta_sql = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "helice_bd.sql"))
        
        # Validar si el archivo existe
        if not os.path.isfile(ruta_sql):
            raise FileNotFoundError(f"Archivo SQL no encontrado en: {ruta_sql}")

        # Crear conexión sin base para ejecutar script de creación
        conexion_sin_db = mysql.connector.connect(**db_config_sin_db)
        
        # Ejecutar script SQL para creación de base y tablas
        ejecutar_script_sql(ruta_sql, conexion_sin_db)
        print("Script SQL ejecutado correctamente.")

        conexion_sin_db.close()

        # Configuración para conexión con la base creada
        db_config_con_db = db_config_sin_db.copy()
        db_config_con_db["database"] = "helice"

        # Conexión final a la base creada
        conexion = mysql.connector.connect(**db_config_con_db)

        if conexion.is_connected():
            print("Se estableció conexión a la base de datos MySQL")

            cursor = conexion.cursor()
            cursor.execute("SELECT DATABASE();")
            db_actual = cursor.fetchone()
            print(f"Base de datos actual: {db_actual[0]}")

        else:
            print("No se pudo establecer conexión")

    except FileNotFoundError as fnfe:
        print(fnfe)
    except Error as e:
        print(f"Error al conectar o ejecutar el script SQL: {e}")
    finally:
        # Cierre seguro de la conexión
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()
            print("Conexión cerrada")
        elif 'conexion_sin_db' in locals() and conexion_sin_db.is_connected():
            conexion_sin_db.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    main()
