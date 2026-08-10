import funciones
from cuerdas import crud


def agregar():

    funciones.titulo("AGREGAR CUERDA")

    nombre = input("Nombre de la cuerda: ").strip()

    x = funciones.leerFloat("Posición X del anclaje: ")
    y = funciones.leerFloat("Posición Y del anclaje: ")
    z = funciones.leerFloat("Posición Z del anclaje: ")

    print("\nLos siguientes datos serán calculados automáticamente.")

    longitud = 0
    angulo_x = 0
    angulo_y = 0
    angulo_z = 0
    tension = 0

    id_material = funciones.leerEntero("ID del material: ")

    id_registro = funciones.leerEntero("ID del registro: ")

    if funciones.confirmar("¿Desea guardar la cuerda?"):

        if crud.insertar(

            nombre,

            x,

            y,

            z,

            longitud,

            angulo_x,

            angulo_y,

            angulo_z,

            tension,

            id_material,

            id_registro

        ):

            funciones.accionExitosa()

        else:

            funciones.accionFallida()


def buscar():

    funciones.titulo("BUSCAR CUERDA")

    id_cuerda = funciones.leerEntero("ID: ")

    cuerda = crud.buscar(id_cuerda)

    if cuerda is None:

        print("\nNo existe esa cuerda.")

    else:

        print("\nID:", cuerda[0])
        print("Nombre:", cuerda[1])
        print("X:", cuerda[2])
        print("Y:", cuerda[3])
        print("Z:", cuerda[4])
        print("Longitud:", cuerda[5])
        print("Ángulo X:", cuerda[6])
        print("Ángulo Y:", cuerda[7])
        print("Ángulo Z:", cuerda[8])
        print("Tensión:", cuerda[9])
        print("Material:", cuerda[10])
        print("Registro:", cuerda[11])

    funciones.espereTecla()


def mostrar():

    funciones.titulo("LISTA DE CUERDAS")

    cuerdas = crud.consultar()

    if len(cuerdas) == 0:

        print("\nNo existen cuerdas registradas.")

    else:

        for cuerda in cuerdas:

            print("-" * 70)

            print("ID:", cuerda[0])
            print("Nombre:", cuerda[1])
            print("X:", cuerda[2])
            print("Y:", cuerda[3])
            print("Z:", cuerda[4])
            print("Longitud:", cuerda[5])
            print("Ángulo X:", cuerda[6])
            print("Ángulo Y:", cuerda[7])
            print("Ángulo Z:", cuerda[8])
            print("Tensión:", cuerda[9])
            print("Material:", cuerda[10])
            print("Registro:", cuerda[11])

    funciones.espereTecla()


def modificar():

    funciones.titulo("MODIFICAR CUERDA")

    id_cuerda = funciones.leerEntero("ID: ")

    cuerda = crud.buscar(id_cuerda)

    if cuerda is None:

        print("\nNo existe esa cuerda.")

        funciones.espereTecla()

        return

    nombre = input(f"Nombre [{cuerda[1]}]: ").strip()

    if nombre == "":
        nombre = cuerda[1]

    x = input(f"X [{cuerda[2]}]: ").strip()

    if x == "":
        x = cuerda[2]
    else:
        x = float(x)

    y = input(f"Y [{cuerda[3]}]: ").strip()

    if y == "":
        y = cuerda[3]
    else:
        y = float(y)

    z = input(f"Z [{cuerda[4]}]: ").strip()

    if z == "":
        z = cuerda[4]
    else:
        z = float(z)

    print("\nLos datos calculados serán actualizados automáticamente.")

    longitud = cuerda[5]
    angulo_x = cuerda[6]
    angulo_y = cuerda[7]
    angulo_z = cuerda[8]
    tension = cuerda[9]

    material = input(f"ID Material [{cuerda[10]}]: ").strip()

    if material == "":
        material = cuerda[10]
    else:
        material = int(material)

    registro = input(f"ID Registro [{cuerda[11]}]: ").strip()

    if registro == "":
        registro = cuerda[11]
    else:
        registro = int(registro)

    if funciones.confirmar("¿Desea actualizar esta cuerda?"):

        if crud.actualizar(

            id_cuerda,

            nombre,

            x,

            y,

            z,

            longitud,

            angulo_x,

            angulo_y,

            angulo_z,

            tension,

            material,

            registro

        ):

            funciones.accionExitosa()

        else:

            funciones.accionFallida()


def eliminar():

    funciones.titulo("ELIMINAR CUERDA")

    id_cuerda = funciones.leerEntero("ID: ")

    if funciones.confirmar("¿Desea eliminar esta cuerda?"):

        if crud.eliminar(id_cuerda):

            funciones.accionExitosa()

        else:

            funciones.accionFallida()


def limpiar():

    funciones.titulo("LIMPIAR TABLA CUERDAS")

    if funciones.confirmar("Esta acción eliminará TODAS las cuerdas"):

        texto = input("\nEscriba CONFIRMAR para continuar: ").upper().strip()

        if texto == "CONFIRMAR":

            if crud.vaciar():

                funciones.accionExitosa()

            else:

                funciones.accionFallida()

        else:

            print("\nOperación cancelada.")

            funciones.espereTecla()


def menu():

    opcion = ""

    while opcion != "7":

        funciones.titulo("CUERDAS")

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
                pass

            case _:
                funciones.opcionInvalida()