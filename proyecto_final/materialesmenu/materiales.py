import funciones

from materialesmenu import crud
from registros import registros


def menu():

    opcion = ""

    while opcion != "7":

        funciones.titulo("MATERIALES")

        print("1.- Agregar")
        print("2.- Buscar")
        print("3.- Mostrar")
        print("4.- Modificar")
        print("5.- Eliminar")
        print("6.- Limpiar")
        print("7.- Regresar\n")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:

            case "1":

                agregar()

            case "2":

                buscar()

            case "3":

                mostrar()

            case "4":

                modificar()

            case "5":

                eliminar()

            case "6":

                limpiar()

            case "7":

                print("\nRegresando al menú principal...")

            case _:

                funciones.opcionInvalida()


def agregar():

    funciones.titulo("AGREGAR MATERIAL")

    nombre = input("Nombre del material: ").strip()

    while nombre == "":

        print("\nEl nombre no puede estar vacío.")

        nombre = input("Nombre del material: ").strip()

    capacidad = funciones.leerFloat(
        "Resistencia máxima en Newtons: "
    )

    while capacidad <= 0:

        print(
            "\nLa resistencia debe ser mayor que cero."
        )

        capacidad = funciones.leerFloat(
            "Resistencia máxima en Newtons: "
        )

    descripcion = input(
        "Descripción: "
    ).strip()

    if crud.agregar(

        nombre,

        capacidad,

        descripcion

    ):

        funciones.accionExitosa()

    else:

        funciones.accionFallida()



def buscar():

    funciones.titulo("BUSCAR MATERIAL")

    id_material = funciones.leerEntero(
        "ID del material: "
    )

    material = crud.buscar(id_material)

    if material is None:

        print("\nNo existe ese material.")

    else:

        print("-" * 70)

        print("ID:", material[0])

        print("Nombre:", material[1])

        print(
            "Resistencia máxima:",
            material[2],
            "N"
        )

        print(
            "Descripción:",
            material[3]
        )

    funciones.espereTecla()


def mostrar():

    funciones.titulo("LISTA DE MATERIALES")

    lista_materiales = crud.consultar()

    if len(lista_materiales) == 0:

        print(
            "\nNo existen materiales registrados."
        )

    else:

        for material in lista_materiales:

            print("-" * 70)

            print("ID:", material[0])

            print("Nombre:", material[1])

            print(
                "Resistencia máxima:",
                material[2],
                "N"
            )

            print(
                "Descripción:",
                material[3]
            )

    funciones.espereTecla()


def modificar():

    funciones.titulo("MODIFICAR MATERIAL")
    print("Ingrese el ID del material que desea modificar. Si no desea modificar un campo, deje el espacio en blanco y presione Enter.\n")

    materiales = crud.consultar()

    if len(materiales) == 0:

        print("\nNo existen materiales registrados.")

        funciones.espereTecla()

        return

    id_material = funciones.leerEntero("ID del material: ")

    material = crud.buscar(id_material)

    if material is None:

        print("\nNo existe ese material.")

        funciones.espereTecla()

        return

    nombre = input(f"\nNombre [{material[1]}]: ").strip()

    if nombre == "":

        nombre = material[1]

    newtons = input(f"Resistencia máxima en Newtons [{material[2]}]: ").strip()

    if newtons == "":

        newtons = material[2]

    descripcion = input(f"Descripción [{material[3]}]: ").strip()

    if descripcion == "":

        descripcion = material[3]

    if funciones.confirmar("¿Guardar cambios?"):

        registros_afectados = crud.modificar(id_material, nombre, descripcion, newtons)

        if registros_afectados is not False:

            for registro in registros_afectados:

                registros.recalcularRegistro(registro)

            funciones.accionExitosa()

        else:

            funciones.accionFallida()

    else:

        print("\nOperación cancelada.")



def eliminar():

    funciones.titulo("ELIMINAR MATERIAL")

    materiales = crud.consultar()

    if len(materiales) == 0:

        print("\nNo existen materiales registrados.")

        funciones.espereTecla()

        return

    id_material = funciones.leerEntero("ID del material: ")

    material = crud.buscar(id_material)

    if material is None:

        print("\nNo existe ese material.")

        funciones.espereTecla()

        return

    print()

    print("Material:", material[1])

    if funciones.confirmar("¿Desea eliminar este material?"):

        if crud.eliminar(id_material):

            funciones.accionExitosa()

        else:

            funciones.accionFallida()

    else:

        print("\nOperación cancelada.")



def limpiar():

    funciones.titulo("LIMPIAR TABLA MATERIALES")

    if funciones.confirmar("Esta acción eliminará TODOS los materiales"):

        texto = input("\nEscriba CONFIRMAR para continuar: ").upper().strip()

        if texto == "CONFIRMAR":

            if crud.vaciar():

                funciones.accionExitosa()

            else:

                funciones.accionFallida()

        else:

            print("\nOperación cancelada.")

    else:

        print("\nOperación cancelada.")