import funciones
from empleados import crud


def agregar():

    funciones.titulo("AGREGAR EMPLEADO")

    opc = True

    while opc:

        nombre = input("Nombre: ").title().strip()

        if funciones.validarTexto(nombre):

            opc = False

        else:

            print("Nombre inválido.")

    opc = True

    while opc:

        apellido_paterno = input("Apellido paterno: ").title().strip()

        if funciones.validarTexto(apellido_paterno):

            opc = False

        else:

            print("Apellido inválido.")

    opc = True

    while opc:

        apellido_materno = input("Apellido materno: ").title().strip()

        if funciones.validarTexto(apellido_materno):

            opc = False

        else:

            print("Apellido inválido.")

    opc = True

    while opc:

        telefono = input("Teléfono: ").strip()

        if funciones.validarTelefono(telefono):

            opc = False

        else:

            print("El teléfono debe contener 10 dígitos.")

    opc = True

    while opc:

        correo = input("Correo: ").strip()

        if funciones.validarCorreo(correo):

            opc = False

        else:

            print("Correo inválido.")

    opc = True

    while opc:

        puesto = input("Puesto: ").title().strip()

        if funciones.validarTexto(puesto):

            opc = False

        else:

            print("Puesto inválido.")

    if funciones.confirmar("¿Desea guardar el empleado?"):

        if crud.insertar(nombre, apellido_paterno, apellido_materno, telefono, correo, puesto):

            funciones.accionExitosa()

        else:

            funciones.accionFallida()

    else:

        print("\nOperación cancelada.")



def buscar():

    funciones.titulo("BUSCAR EMPLEADO")

    id_empleado = funciones.leerEntero("ID: ")

    empleado = crud.buscar(id_empleado)

    if empleado is None:

        print("\nNo existe ese empleado.")

    else:

        print("\nID:", empleado[0])
        print("Nombre:", empleado[1])
        print("Apellido paterno:", empleado[2])
        print("Apellido materno:", empleado[3])
        print("Teléfono:", empleado[4])
        print("Correo:", empleado[5])
        print("Puesto:", empleado[6])
        print("Fecha:", empleado[7])

    funciones.espereTecla()


def mostrar():

    funciones.titulo("LISTA DE EMPLEADOS")

    empleados = crud.consultar()

    if len(empleados) == 0:

        print("\nNo existen empleados registrados.")

    else:

        for empleado in empleados:

            print("-" * 60)

            print("ID:", empleado[0])
            print("Nombre:", empleado[1])
            print("Apellido paterno:", empleado[2])
            print("Apellido materno:", empleado[3])
            print("Teléfono:", empleado[4])
            print("Correo:", empleado[5])
            print("Puesto:", empleado[6])
            print("Fecha:", empleado[7])

    funciones.espereTecla()


def modificar():

    funciones.titulo("MODIFICAR EMPLEADO")
    print("Ingrese el ID del empleado que desea modificar. Si no desea modificar un campo, deje el espacio en blanco y presione Enter.\n")

    id_empleado = funciones.leerEntero("ID: ")

    empleado = crud.buscar(id_empleado)

    if empleado is None:

        print("\nEmpleado no encontrado.")

        funciones.espereTecla()

        return

    nombre = input(f"Nombre [{empleado[1]}]: ").title().strip()
    if nombre == "":
        nombre = empleado[1]

    apellido_paterno = input(f"Apellido paterno [{empleado[2]}]: ").title().strip()
    if apellido_paterno == "":
        apellido_paterno = empleado[2]

    apellido_materno = input(f"Apellido materno [{empleado[3]}]: ").title().strip()
    if apellido_materno == "":
        apellido_materno = empleado[3]

    telefono = input(f"Teléfono [{empleado[4]}]: ").strip()
    if telefono == "":
        telefono = empleado[4]

    correo = input(f"Correo [{empleado[5]}]: ").strip()
    if correo == "":
        correo = empleado[5]

    puesto = input(f"Puesto [{empleado[6]}]: ").title().strip()
    if puesto == "":
        puesto = empleado[6]

    if funciones.confirmar("¿Desea actualizar este empleado?"):

        if crud.actualizar(
            id_empleado,
            nombre,
            apellido_paterno,
            apellido_materno,
            telefono,
            correo,
            puesto
        ):

            funciones.accionExitosa()

        else:

            funciones.accionFallida()


def eliminar():

    funciones.titulo("ELIMINAR EMPLEADO")

    empleados = crud.consultar()

    if len(empleados) == 0:

        print("\nNo existen empleados registrados.")

        funciones.espereTecla()

        return

    print("Ingrese el ID del empleado que desea eliminar.\n")

    id_empleado = funciones.leerEntero("ID: ")

    empleado = crud.buscar(id_empleado)

    if empleado is None:

        print("\nNo existe un empleado con ese ID.")

        funciones.espereTecla()

        return

    if funciones.confirmar("¿Desea eliminar este empleado?"):

        if crud.eliminar(id_empleado):

            funciones.accionExitosa()

        else:

            funciones.accionFallida()

    else:

        print("\nOperación cancelada.")


def limpiar():

    funciones.titulo("LIMPIAR TABLA EMPLEADOS")

    if funciones.confirmar("Esta acción eliminará TODOS los empleados"):

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

        funciones.titulo("EMPLEADOS")

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