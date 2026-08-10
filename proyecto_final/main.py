import funciones

from empleados import empleados
from registros import registros
from reportes import reportes
from materialesmenu import materiales 

def menuPrincipal():

    funciones.titulo("SISTEMA DE GESTIÓN DE TENSIONES")
    print("1.- Registros")
    print("2.- Empleados")
    print("3.- Reportes")
    print("4.- Materiales")
    print("5.- Salir\n")
    return input("Seleccione una opción: ").strip()


opcion = ""

while opcion != "5":

    opcion = menuPrincipal()

    match opcion:

        case "1":

            registros.menu()

        case "2":

            empleados.menu()

        case "3":

            reportes.menu()

        case "4":
            
            materiales.menu()

        case "5":

            print("\nGracias por utilizar el sistema.")

        case _:

            funciones.opcionInvalida()