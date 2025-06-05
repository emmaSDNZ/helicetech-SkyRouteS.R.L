#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sistema de gestion de pasajes de la Empresa SkyRoute S.R.L.
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PROPOSITO:
# Este sistema permite gestionar la venta de pasajes, el registro de clientes, los destinos disponibles y aplicar el boton de arrepentimiento para anular ventas dentro del plazo permitido.
#
# INSTALACION Y EJECUCION:
# 1.Requiere tener Python 3.10 instalado.
# 2.Crear y activar un entorno virtual.
# 3.Ejecutar Python.
# 4.Guardar este archivo como "main.py".

# INTEGRANTES DEL GRUPO:
# -Luciana Goldraij- DNI:49262403
# -Sol Milagros Baigorria- DNI:45095087
# -Luciano Castillo- DNI:43062186
# -Isaias Emanuel Sudañez- DNI:39231001
from gestionar_cliente import gestionar_cliente
from gestionar_destino import gestionar_destino
from gestionar_ventas import gestionar_ventas
from gestionar_ventas import boton_de_arrepentimiento
from gestionar_ventas import consultar_ventas
from sistema import ver_reporte_general
from sistema import acerca_del_sistema
from sistema import salir

def menu_principal():
    print("BIENVENIDOS A SkyRoute Sistema de Gestión de Pasajes")
    print("1) Gestionar Clientes")
    print("2) Gestionar Destinos")
    print("3) Gestionar Ventas")
    print("4) Consultar Ventas")
    print("5) Boton de Arrepentimiento")
    print("6) Ver Reporte General")
    print("7) Acerca del sistema")
    print("8) Salir.")
        
def menu():
    while True:
        menu_principal()
        opcion=input("Por favor elija una opcion: ")
        if opcion=="1":
            gestionar_cliente()
        elif opcion=="2":
            gestionar_destino()
        elif opcion=="3":
            gestionar_ventas()
        elif opcion=="4":
            consultar_ventas()
        elif opcion=="5":
            boton_de_arrepentimiento()
        elif opcion=="6":
            ver_reporte_general()
        elif opcion=="7":
            acerca_del_sistema()
        elif opcion=="8":
            salir()
            break
        else:
            print("opcion invalida")

menu()

