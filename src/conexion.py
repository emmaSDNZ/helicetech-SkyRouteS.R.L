import mysql.connector
from mysql.connector import Error

def conectar():
    """
    Establece y devuelve una conexión a la base de datos MySQL.

    Parámetros:
    ----------
    No recibe parámetros.

    Retorna:
    -------
    mysql.connector.connection.MySQLConnection o None
        Objeto de conexión a la base de datos si la conexión es exitosa.
        Retorna None si ocurre un error al intentar conectar.

    Comportamiento:
    --------------
    Intenta conectar a la base de datos MySQL utilizando los parámetros
    configurados (host, usuario, contraseña, base de datos y puerto).
    Si la conexión se establece correctamente, imprime un mensaje
    indicando éxito y retorna el objeto conexión.
    En caso de error, imprime el error y retorna None.
    """
     
    config = {
        "host": "localhost",
        "user": "root",
        "database": "helice",
        "password": "1234",
        "port": 3306
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            print("Conexion exitosa. Base de datos: helice")
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

conectar()
