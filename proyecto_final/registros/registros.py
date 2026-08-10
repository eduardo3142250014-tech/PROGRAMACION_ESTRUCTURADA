import math
import funciones
from registros import crud
from registros import calculos
from empleados import crud as crudEmpleados
import materiales

def agregar():

    funciones.titulo("NUEVO REGISTRO")

    print("Ingrese la información del proyecto y del candelabro que desea analizar.\n")

    nombre_proyecto = ""

    while len(nombre_proyecto) == 0:

        nombre_proyecto = input("Nombre del proyecto: ").strip()

        if len(nombre_proyecto) == 0:

            print("\nEl nombre del proyecto es obligatorio.")


    descripcion = ""

    while len(descripcion) == 0:

        descripcion = input("Descripción del proyecto: ").strip()

        if len(descripcion) == 0:

            print("\nLa descripción es obligatoria.")


    masa = 0

    while masa <= 0:

        masa = funciones.leerFloat("\nMasa del candelabro en kilogramos (kg): ")

        if masa <= 0:

            print("\nLa masa debe ser mayor que cero.")


    funciones.titulo("POSICIÓN DEL CANDELABRO")

    print("Indique la posición donde se encuentra el candelabro.\n")

    x = funciones.leerFloat("Coordenada X: ")
    y = funciones.leerFloat("Coordenada Y: ")
    z = funciones.leerFloat("Coordenada Z: ")


    empleados = crudEmpleados.consultar()

    if len(empleados) == 0:

        print("\nNo existen empleados registrados. Primero debe registrar al menos un empleado.")

        funciones.espereTecla()

        return


    funciones.titulo("SELECCIONAR EMPLEADO RESPONSABLE")

    print("Seleccione al empleado responsable del proyecto.\n")

    for empleado_actual in empleados:

        print(f"{empleado_actual[0]}. {empleado_actual[1]} {empleado_actual[2]}")


    empleado = None

    while empleado is None:

        id_empleado = funciones.leerEntero("\nID del empleado: ")

        empleado = crudEmpleados.buscar(id_empleado)

        if empleado is None:

            print("\nEl empleado seleccionado no existe.")


    lista_materiales = materiales.obtenerMateriales()

    if len(lista_materiales) == 0:

        print("\nNo existen materiales registrados. Primero debe registrar al menos un material.")

        funciones.espereTecla()

        return


    funciones.titulo("CONFIGURACIÓN DE LAS CUERDAS")

    print("Indique cuántas cuerdas sostendrán el candelabro.")

    print("El sistema requiere al menos 1 cuerda para realizar el análisis.\n")


    numero_cuerdas = 0

    while numero_cuerdas < 1:

        numero_cuerdas = funciones.leerEntero("Número total de cuerdas: ")

        if numero_cuerdas < 3:

            print("\nDebe registrar un mínimo de 3 cuerdas.")


    lista_cuerdas = []

    indice = 1


    while indice <= numero_cuerdas:

        funciones.titulo(f"CONFIGURAR CUERDA {indice}")

        print(f"Ingrese la posición del punto donde estará sujetada la Cuerda {indice}.")

        print("El punto de anclaje debe estar por encima del candelabro.\n")


        cuerda_valida = False


        while cuerda_valida == False:

            x_anclaje = funciones.leerFloat("Coordenada X del anclaje: ")

            y_anclaje = funciones.leerFloat("Coordenada Y del anclaje: ")

            z_anclaje = funciones.leerFloat("Coordenada Z del anclaje: ")


            if z_anclaje <= z:

                print("\nEl punto de anclaje debe estar por encima de la posición del candelabro.")

            else:

                repetida = False


                for cuerda in lista_cuerdas:

                    if cuerda["x"] == x_anclaje and cuerda["y"] == y_anclaje and cuerda["z"] == z_anclaje:

                        repetida = True


                if repetida:

                    print("\nYa existe una cuerda registrada con esas mismas coordenadas.")

                    print("Ingrese una posición diferente para esta cuerda.")

                else:

                    datos = calculos.obtenerDatosCuerda((x, y, z), (x_anclaje, y_anclaje, z_anclaje))


                    if datos["longitud"] <= 0:

                        print("\nLa longitud calculada de la cuerda debe ser mayor que cero.")

                    else:

                        materiales.mostrarMateriales()

                        print("\nSeleccione el material que se utilizará para esta cuerda.")

                        id_material = 0


                        while materiales.existe(id_material) == False:

                            id_material = funciones.leerEntero("ID del material: ")

                            if materiales.existe(id_material) == False:

                                print("\nEl material seleccionado no existe.")


                        datos["nombre"] = f"Cuerda {indice}"

                        datos["x"] = x_anclaje

                        datos["y"] = y_anclaje

                        datos["z"] = z_anclaje

                        datos["id_material"] = id_material


                        lista_cuerdas.append(datos)


                        print(f"\nLa Cuerda {indice} fue configurada correctamente.")

                        cuerda_valida = True

                        indice += 1


    funciones.titulo("RESUMEN DEL PROYECTO")

    print("Revise cuidadosamente la siguiente información antes de realizar el análisis.\n")

    print(f"Nombre del proyecto: {nombre_proyecto}")

    print(f"Descripción: {descripcion}")

    print(f"Masa del candelabro: {masa} kg")

    print(f"Empleado responsable: {empleado[1]} {empleado[2]}")

    print(f"Posición del candelabro: ({x}, {y}, {z})")

    print(f"Número total de cuerdas: {numero_cuerdas}")


    print("\n========== CONFIGURACIÓN DE LAS CUERDAS ==========")


    for cuerda in lista_cuerdas:

        print(f"\n{cuerda['nombre']}")

        print(f"Punto de anclaje: ({cuerda['x']}, {cuerda['y']}, {cuerda['z']})")

        print(f"Longitud calculada: {round(cuerda['longitud'], 3)} m")


        material = None


        for material_actual in lista_materiales:

            if material_actual[0] == cuerda["id_material"]:

                material = material_actual


        if material is not None:

            print(f"Material seleccionado: {material[1]}")

            print(f"Resistencia máxima del material: {material[2]} N")

        else:

            print(f"Material seleccionado: ID {cuerda['id_material']}")


    if funciones.confirmar("\n¿Los datos son correctos y desea realizar el análisis?") == False:

        print("\nOperación cancelada.")

        funciones.espereTecla()

        return


    funciones.titulo("ANÁLISIS")

    print("El sistema está calculando las tensiones y factores de seguridad de las cuerdas.\n")


    try:

        lista_cuerdas, conclusion = calculos.realizarAnalisis(masa, lista_cuerdas)


    except Exception as err:

        print("\nOcurrió un error durante el análisis.")

        print("No se guardó ningún dato del proyecto.")

        print(f"\nDetalle: {err}")

        funciones.espereTecla()

        return


    print("\nEl análisis fue realizado correctamente.\n")

    print(f"Resultado del sistema: {'VIABLE' if conclusion['viable'] else 'NO VIABLE'}")

    print(f"Factor de seguridad mínimo obtenido: {round(conclusion['factor_minimo'], 2)}")


    if funciones.confirmar("\n¿Desea guardar este proyecto y sus resultados?") == False:

        print("\nEl proyecto no fue almacenado.")

        funciones.espereTecla()

        return


    id_registro = crud.insertar(nombre_proyecto, descripcion, masa, x, y, z, numero_cuerdas, "VIABLE" if conclusion["viable"] else "NO VIABLE", conclusion["factor_minimo"], conclusion["viable"], id_empleado)


    if id_registro is None:

        print("\nNo fue posible guardar el proyecto.")

        funciones.accionFallida()

        funciones.espereTecla()

        return


    guardado_correcto = True


    for cuerda in lista_cuerdas:

        respuesta = crud.insertarCuerda(cuerda["nombre"], cuerda["x"], cuerda["y"], cuerda["z"], cuerda["longitud"], cuerda["angulo_x"], cuerda["angulo_y"], cuerda["angulo_z"], cuerda["tension"], cuerda["id_material"], id_registro)


        if respuesta == False:

            guardado_correcto = False

            print(f"\nNo fue posible guardar {cuerda['nombre']}.")


    funciones.titulo("RESULTADO FINAL")


    if guardado_correcto:

        print("El proyecto y todas sus cuerdas fueron registrados correctamente.\n")

        print(f"ID asignado al proyecto: {id_registro}")

        print(f"Resultado del análisis: {'VIABLE' if conclusion['viable'] else 'NO VIABLE'}")

        print(f"Factor de seguridad mínimo: {round(conclusion['factor_minimo'], 2)}")

        funciones.accionExitosa()


    else:

        print("El proyecto fue registrado, pero una o más cuerdas no pudieron almacenarse.")

        funciones.accionFallida()




def buscar():

    funciones.titulo("BUSCAR REGISTRO")

    id_registro = funciones.leerEntero("ID del registro: ")

    registro = crud.buscar(id_registro)

    if registro is None:

        print("\nNo existe ese registro.")

    else:

        print("\n========== REGISTRO ==========\n")

        print(f"ID: {registro[0]}")
        print(f"Proyecto: {registro[1]}")
        print(f"Descripción: {registro[2]}")
        print(f"Masa: {registro[3]} kg")
        print(f"Posición: ({registro[4]}, {registro[5]}, {registro[6]})")
        print(f"Cuerdas: {registro[7]}")
        print(f"Resultado: {registro[8]}")
        print(f"Factor de seguridad: {registro[9]}")
        print(f"Viable: {'SI' if registro[10] else 'NO'}")
        print(f"Fecha: {registro[11]}")
        print(f"Empleado: {registro[12]}")
        cuerdas = crud.consultarCuerdas(registro[0])

        print("\n========== CUERDAS ==========")

        if len(cuerdas) == 0:

            print("\nEste registro no tiene cuerdas.")

        else:

            for cuerda in cuerdas:

                print()

                print(f"ID: {cuerda[0]}")

                print(f"Nombre: {cuerda[1]}")

                print(
                    f"Posición: "
                    f"({cuerda[2]}, {cuerda[3]}, {cuerda[4]})"
                )

                print(
                    f"Longitud: {round(cuerda[5],3)} m"
                )

                print(
                    f"Tensión: {round(cuerda[9],2)} N"
                )

                print(
                    f"Material: {cuerda[10]}"
                )

                print("-" * 40)

    funciones.espereTecla()


def mostrar():

    funciones.titulo("REGISTROS")

    registros = crud.consultar()

    if len(registros) == 0:
        print("\nNo existen registros.")

    else:

        for registro in registros:

            print("=" * 60)

            print(f"ID: {registro[0]}")
            print(f"Proyecto: {registro[1]}")
            print(f"Descripción: {registro[2]}")
            print(f"Masa: {registro[3]} kg")
            print(f"Posición: ({registro[4]}, {registro[5]}, {registro[6]})")
            print(f"Cantidad de cuerdas: {registro[7]}")
            print(f"Resultado: {registro[8]}")
            print(f"Factor de seguridad: {registro[9]}")
            print(f"Empleado: {registro[12]}")

            cuerdas = crud.consultarCuerdas(registro[0])

            print("\nCUERDAS")

            if len(cuerdas) == 0:
                print("No existen cuerdas.")

            else:
                for cuerda in cuerdas:
                    print("-" * 40)
                    print(f"Nombre: {cuerda[1]}")
                    print(
                        f"Posición: "
                        f"({cuerda[2]}, {cuerda[3]}, {cuerda[4]})"
                    )
                    print(
                        f"Longitud: "
                        f"{round(cuerda[5],3)} m"
                    )
                    print(
                        f"Tensión: "
                        f"{round(cuerda[9],2)} N"
                    )
                    print(
                        f"Material: "
                        f"{cuerda[10]}"
                    )

            print("=" * 60)

    funciones.espereTecla()


def modificar():

    funciones.titulo("MODIFICAR REGISTRO")
    id_registro = funciones.leerEntero("ID del registro: ")

    registro = crud.buscar(id_registro)

    if registro is None:

        print("\nEse registro no existe.")

        funciones.espereTecla()

        return


    funciones.titulo("REGISTRO ENCONTRADO")

    print(f"\nID: {registro[0]}")

    print(f"Proyecto: {registro[1]}")

    print(f"Descripción: {registro[2]}")

    print(f"Masa: {registro[3]} kg")

    print(
        f"Posición: "
        f"({registro[4]}, "
        f"{registro[5]}, "
        f"{registro[6]})"
    )

    print(f"Cuerdas: {registro[7]}")

    print(f"Resultado: {registro[8]}")

    print(
        f"Factor de seguridad: "
        f"{registro[9]}"
    )

    print(
        f"Viable: "
        f"{'SI' if registro[10] else 'NO'}"
    )

    print(f"Empleado: {registro[12]}")


    print("\n========== OPCIONES ==========\n")

    print("1. Nombre del proyecto")

    print("2. Descripción")

    print("3. Masa del candelabro")

    print("4. Posición del candelabro")

    print("5. Empleado responsable")

    print("6. Administrar cuerdas")

    print("7. Cancelar")


    opcion = input("\nSeleccione una opción: ").strip()


    match opcion:

        case "1":

            modificarProyecto(id_registro)

        case "2":

            modificarDescripcion(id_registro)

        case "3":

            modificarMasa(id_registro)

        case "4":

            modificarPosicion(id_registro)

        case "5":

            modificarEmpleado(id_registro)

        case "6":

            menuCuerdas(id_registro)

        case "7":

            return

        case _:

            funciones.opcionInvalida()


def eliminar():

    funciones.titulo("ELIMINAR REGISTRO")

    id_registro = funciones.leerEntero("ID del registro: ")

    registro = crud.buscar(id_registro)

    if registro is None:

        print("\nEse registro no existe.")

    else:

        print("\nTambién se eliminarán")

        print("todas las cuerdas asociadas.")

        if funciones.confirmar("¿Desea continuar?"):

            respuesta = crud.eliminar(id_registro)

            if respuesta:

                funciones.accionExitosa()

            else:

                funciones.accionFallida()



def limpiar():

    funciones.titulo("LIMPIAR TABLA")

    print("\nEsta operación eliminará")

    print("todos los registros")

    print("y todas las cuerdas.")

    if funciones.confirmar("¿Desea continuar?"):

        texto = input("\nEscriba ELIMINAR para confirmar: ").upper().strip()

        if texto == "ELIMINAR":

            respuesta = crud.vaciar()

            if respuesta:

                funciones.accionExitosa()

            else:

                funciones.accionFallida()

        else:

            print("\nOperación cancelada.")

    else:

        print("\nOperación cancelada.")

def menu():

    opcion = ""

    while opcion != "7":

        funciones.titulo("REGISTROS")

        print("1.- Nuevo registro")

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

def modificarProyecto(id_registro):

    funciones.titulo("MODIFICAR PROYECTO")

    registro = crud.buscar(id_registro)

    print(f"\nNombre actual: {registro[1]}")

    nuevo_nombre = ""

    while len(nuevo_nombre.strip()) == 0:

        nuevo_nombre = input("\nNuevo nombre: ").strip()

        if len(nuevo_nombre) == 0:

            print("\nEl nombre no puede estar vacío.")

    if funciones.confirmar("¿Guardar cambios?") == False:

        print("\nOperación cancelada.")

        funciones.espereTecla()

        return

    if crud.actualizarProyecto(id_registro,nuevo_nombre):

        funciones.accionExitosa()

    else:

        funciones.accionFallida()




def modificarDescripcion(id_registro):

    funciones.titulo("MODIFICAR DESCRIPCIÓN")

    registro = crud.buscar(id_registro)

    print(f"\nDescripción actual:\n")

    print(registro[2])

    nueva_descripcion = ""

    while len(nueva_descripcion.strip()) == 0:

        nueva_descripcion = input("\nNueva descripción: ").strip()

        if len(nueva_descripcion) == 0:

            print("\nLa descripción no puede estar vacía.")

    if funciones.confirmar("¿Guardar cambios?") == False:

        print("\nOperación cancelada.")

        funciones.espereTecla()

        return

    if crud.actualizarDescripcion(id_registro,nueva_descripcion):

        funciones.accionExitosa()

    else:

        funciones.accionFallida()



def modificarEmpleado(id_registro):

    funciones.titulo("MODIFICAR EMPLEADO")

    empleados = crudEmpleados.consultar()

    for empleado in empleados:

        print(
            f"{empleado[0]}. "
            f"{empleado[1]} "
            f"{empleado[2]}"
        )

    empleado = None

    while empleado is None:

        id_empleado = funciones.leerEntero("\nSeleccione el empleado: ")

        empleado = crudEmpleados.buscar(id_empleado)

        if empleado is None:

            print("\nEse empleado no existe.")

    if funciones.confirmar("¿Guardar cambios?") == False:

        print("\nOperación cancelada.")

        funciones.espereTecla()

        return

    if crud.actualizarEmpleado(id_registro,id_empleado):

        funciones.accionExitosa()

    else:

        funciones.accionFallida()


def modificarMasa(id_registro):

    funciones.titulo("MODIFICAR MASA")

    registro = crud.buscar(id_registro)

    print(f"\nMasa actual: {registro[3]} kg")

    nueva_masa = 0

    while nueva_masa <= 0:

        nueva_masa = funciones.leerFloat("\nNueva masa (kg): ")

        if nueva_masa <= 0:

            print("\nLa masa debe ser mayor que cero.")

    if funciones.confirmar("¿Guardar cambios?") == False:

        print("\nOperación cancelada.")

        funciones.espereTecla()

        return

    if crud.actualizarMasa(id_registro,nueva_masa):

        print("\nRecalculando análisis...")

        recalcularRegistro(id_registro)

        funciones.accionExitosa()

    else:

        funciones.accionFallida()




def modificarPosicion(id_registro):

    funciones.titulo("MODIFICAR POSICIÓN")

    registro = crud.buscar(id_registro)

    print(
        f"\nPosición actual: "
        f"({registro[4]}, {registro[5]}, {registro[6]})"
    )

    x = funciones.leerFloat("\nNueva X: ")

    y = funciones.leerFloat("Nueva Y: ")

    z = funciones.leerFloat("Nueva Z: ")

    if funciones.confirmar("¿Guardar cambios?") == False:

        print("\nOperación cancelada.")

        funciones.espereTecla()

        return

    if crud.actualizarPosicion(id_registro,x,y,z):

        print("\nRecalculando análisis...")

        recalcularRegistro(id_registro)

        funciones.accionExitosa()

    else:

        funciones.accionFallida()


def recalcularRegistro(id_registro):

    registro = crud.buscar(id_registro)

    if registro is None:

        return None


    masa = registro[3]

    punto_candelabro = (registro[4],registro[5],registro[6])


    cuerdas_bd = crud.consultarCuerdas(id_registro)

    if len(cuerdas_bd) == 0:

        return None


    lista_cuerdas = []
    for cuerda_bd in cuerdas_bd:

        punto_anclaje = (cuerda_bd[2],cuerda_bd[3],cuerda_bd[4])

        datos = calculos.obtenerDatosCuerda(punto_candelabro,punto_anclaje)

        datos["id_cuerda"] = cuerda_bd[0]

        datos["nombre"] = cuerda_bd[1]

        datos["x"] = cuerda_bd[2]

        datos["y"] = cuerda_bd[3]

        datos["z"] = cuerda_bd[4]

        datos["id_material"] = cuerda_bd[10]

        lista_cuerdas.append(datos)
    lista_cuerdas, conclusion = (calculos.realizarAnalisis(masa,lista_cuerdas,False))
    for cuerda in lista_cuerdas:

        crud.actualizarDatosCuerda(cuerda["id_cuerda"],cuerda)


    crud.actualizarAnalisis(

        id_registro,

        len(lista_cuerdas),

        "VIABLE"
        if conclusion["viable"]
        else
        "NO VIABLE",

        conclusion["factor_minimo"],

        conclusion["viable"]

    )


    return conclusion
def menuCuerdas(id_registro):

    opc = ""

    while opc != "4":

        funciones.titulo("ADMINISTRAR CUERDAS")

        cuerdas = crud.consultarCuerdas(id_registro)

        if len(cuerdas) == 0:

            print("\nNo existen cuerdas registradas.")

        else:

            print("\nCUERDAS ACTUALES\n")

            contador = 1

            while contador <= len(cuerdas):

                cuerda = cuerdas[contador-1]

                print(
                    f"{contador}. "
                    f"{cuerda[1]}"
                )

                contador += 1

        print("\n========== OPCIONES ==========\n")

        print("1. Modificar cuerda")

        print("2. Agregar cuerda")

        print("3. Eliminar cuerda")

        print("4. Regresar")

        opc = input("\nSeleccione una opción: ").strip()

        match opc:

            case "1":

                modificarCuerda(id_registro)

            case "2":

                agregarCuerda(id_registro)

            case "3":

                eliminarCuerda(id_registro)

            case "4":
                return 

            case _:

                funciones.opcionInvalida()

def modificarCuerda(id_registro):

    funciones.titulo("MODIFICAR CUERDA")

    cuerdas = crud.consultarCuerdas(id_registro)

    if len(cuerdas) == 0:

        print("\nNo existen cuerdas registradas.")

        funciones.espereTecla()

        return


    contador = 1

    while contador <= len(cuerdas):

        cuerda = cuerdas[contador - 1]

        print(
            f"{contador}. "
            f"{cuerda[1]}"
        )

        contador += 1


    opcion = 0

    while opcion < 1 or opcion > len(cuerdas):

        opcion = funciones.leerEntero("\nSeleccione una cuerda: ")

        if opcion < 1 or opcion > len(cuerdas):

            print("\nOpción inválida.")


    cuerda = cuerdas[opcion - 1]


    print("\n========== MODIFICAR ==========\n")

    print("1. Posición")

    print("2. Material")

    print("3. Cancelar")


    opcion = input("\nSeleccione una opción: ").strip()


    match opcion:

        case "1":

            x = funciones.leerFloat("\nNueva X: ")

            y = funciones.leerFloat("Nueva Y: ")

            z = funciones.leerFloat("Nueva Z: ")

            if funciones.confirmar("¿Guardar cambios?"):

                if crud.actualizarPosicionCuerda(cuerda[0],x,y,z):

                    recalcularRegistro(id_registro)

                    funciones.accionExitosa()

                else:

                    funciones.accionFallida()
        case "2":

            materiales.mostrarMateriales()

            id_material = 0

            while not materiales.existe(id_material):

                id_material = funciones.leerEntero("\nMaterial: ")

                if not materiales.existe(id_material):

                    print("\nMaterial inexistente.")

            if funciones.confirmar("¿Guardar cambios?"):

                if crud.actualizarMaterialCuerda(cuerda[0],id_material):

                    recalcularRegistro(id_registro)

                    funciones.accionExitosa()

                else:

                    funciones.accionFallida()


        case "3":

            return


        case _:

            funciones.opcionInvalida()

def agregarCuerda(id_registro):

    funciones.titulo("AGREGAR CUERDA")

    registro = crud.buscar(id_registro)

    punto_candelabro = (
        registro[4],
        registro[5],
        registro[6]
    )

    materiales.mostrarMateriales()

    x = funciones.leerFloat("\nX del anclaje: ")

    y = funciones.leerFloat("Y del anclaje: ")

    z = funciones.leerFloat("Z del anclaje: ")

    if z <= punto_candelabro[2]:

        print("\nEl anclaje debe estar por encima del candelabro.")

        funciones.espereTecla()

        return

    id_material = 0

    while not materiales.existe(id_material):

        id_material = funciones.leerEntero("\nMaterial: ")

        if not materiales.existe(id_material):

            print("\nMaterial inexistente.")

    datos = calculos.obtenerDatosCuerda(punto_candelabro,(x, y, z))

    cuerdas = crud.consultarCuerdas(id_registro)

    nombre = f"Cuerda {len(cuerdas)+1}"

    if crud.insertarCuerda(

        nombre,

        x,

        y,

        z,

        datos["longitud"],

        datos["angulo_x"],

        datos["angulo_y"],

        datos["angulo_z"],

        0,

        id_material,

        id_registro
    ):

        recalcularRegistro(id_registro)

        funciones.accionExitosa()

    else:

        funciones.accionFallida()

def eliminarCuerda(id_registro):

    funciones.titulo("ELIMINAR CUERDA")

    cuerdas = crud.consultarCuerdas(id_registro)

    if len(cuerdas) <= 1:

        print("\nNo es posible eliminar una cuerda.")

        print("El sistema debe conservar al menos 1 cuerda.")

        funciones.espereTecla()

        return


    contador = 1

    while contador <= len(cuerdas):

        cuerda = cuerdas[contador-1]

        print(
            f"{contador}. "
            f"{cuerda[1]}"
        )

        contador += 1


    opcion = 0

    while opcion < 1 or opcion > len(cuerdas):

        opcion = funciones.leerEntero("\nSeleccione una cuerda: ")

        if opcion < 1 or opcion > len(cuerdas):

            print("\nOpción inválida.")


    cuerda = cuerdas[opcion-1]


    if funciones.confirmar(f"¿Eliminar {cuerda[1]}?") == False:

        print("\nOperación cancelada.")

        funciones.espereTecla()

        return


    if crud.eliminarCuerda(cuerda[0]):

        recalcularRegistro(id_registro)

        funciones.accionExitosa()

    else:

        funciones.accionFallida()