import mysql.connector
def conectar():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="helice"
    )

    print(mydb)