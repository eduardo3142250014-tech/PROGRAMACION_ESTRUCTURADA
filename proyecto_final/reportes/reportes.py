import funciones

from reportes import txt
from reportes import pdf
from reportes import excel


def menu():

    opcion = ""
    while opcion != "4":

        funciones.titulo("REPORTES")
        print("1.- Generar TXT")
        print("2.- Generar PDF")
        print("3.- Generar Excel")
        print("4.- Regresar\n")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:

            case "1":
                txt.generar()
            case "2":
                pdf.generar()
            case "3":
                excel.generar()
            case "4":
                print("\nRegresando al menú principal...")
            case _:

                funciones.opcionInvalida()