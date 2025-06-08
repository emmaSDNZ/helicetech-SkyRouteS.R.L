import mysql.connector
from mysql.connector import Error

def conectar():
    """
    Devuelve una conexión MySQL.
    
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