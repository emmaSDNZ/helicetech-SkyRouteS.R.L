<<<<<<< HEAD
import mysql.connector
def conectar():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="helice"
    )

    print(mydb)
=======
#conexion de mysql
import mysql.connector
from mysql.connector import Error

def conectar():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="helice"
    )
    return(mydb)
conectar()
>>>>>>> dev
