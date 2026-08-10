import math

from config import GRAVEDAD


def calcularVector(punto_candelabro, punto_anclaje):


    vx = float(punto_anclaje[0]) - float(punto_candelabro[0])
    vy = float(punto_anclaje[1]) - float(punto_candelabro[1])
    vz = float(punto_anclaje[2]) - float(punto_candelabro[2])

    return (vx, vy, vz)


def calcularLongitud(vector):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)

def calcularVectorUnitario(vector):

    longitud = calcularLongitud(vector)

    if longitud == 0:
        raise ValueError(
            "La longitud del vector no puede ser cero."
        )
    ux = vector[0] / longitud
    uy = vector[1] / longitud
    uz = vector[2] / longitud
    return (ux, uy, uz)

def calcularAngulos(vector_unitario):


    ux = vector_unitario[0]
    uy = vector_unitario[1]
    uz = vector_unitario[2]

    angulo_x = math.degrees(math.acos(ux))
    angulo_y = math.degrees(math.acos(uy))
    angulo_z = math.degrees(math.acos(uz))

    return (angulo_x,angulo_y,angulo_z)


def calcularPeso(masa):

    return float(masa) * GRAVEDAD


def obtenerDatosCuerda(punto_candelabro,punto_anclaje):
    vector = calcularVector(
        punto_candelabro,
        punto_anclaje
    )

    longitud = calcularLongitud(vector)
    unitario = calcularVectorUnitario(vector)
    angulos = calcularAngulos(unitario)

    return {
        "vector": vector,
        "longitud": longitud,
        "unitario": unitario,
        "angulo_x": angulos[0],
        "angulo_y": angulos[1],
        "angulo_z": angulos[2],
        "uz": unitario[2]
    }


def mostrarDatosCuerda(datos):
    print("\n==============================")
    print("VECTOR")
    print(datos["vector"])
    print("\nLONGITUD")
    print(round(datos["longitud"],3))
    print("\nVECTOR UNITARIO")
    print(datos["unitario"])
    print("\nÁNGULOS")
    print("X:",round(datos["angulo_x"],2),"°")
    print("Y:",round(datos["angulo_y"],2),"°")
    print("Z:",round(datos["angulo_z"],2),"°")
    print("==============================")
    
def calcularContribucionVertical(lista_cuerdas):
    suma = 0
    for cuerda in lista_cuerdas:
        suma += abs(cuerda["uz"])

    return suma


def calcularPorcentajes(lista_cuerdas):
    suma = calcularContribucionVertical(lista_cuerdas)
    if suma == 0:
        raise ValueError("No existe componente vertical.")

    for cuerda in lista_cuerdas:
        porcentaje = abs(cuerda["uz"]) / suma
        cuerda["porcentaje"] = porcentaje
    return lista_cuerdas


def calcularTensiones(lista_cuerdas,peso):

    for cuerda in lista_cuerdas:
        tension = peso * cuerda["porcentaje"]
        cuerda["tension"] = tension
    return lista_cuerdas


def calcularFactorSeguridad(lista_cuerdas,materiales):


    for cuerda in lista_cuerdas:
        id_material = cuerda["id_material"]
        resistencia = materiales[id_material]
        cuerda["resistencia"] = resistencia
        cuerda["factor_seguridad"] = (resistencia / cuerda["tension"])

    return lista_cuerdas


def verificarSistema(lista_cuerdas,factor_minimo=3):
    sistema_viable = True
    for cuerda in lista_cuerdas:
        if cuerda["factor_seguridad"] < factor_minimo:
            cuerda["viable"] = False
            sistema_viable = False
        else:
            cuerda["viable"] = True
    return sistema_viable


def obtenerMayorTension(lista_cuerdas):
    mayor = lista_cuerdas[0]
    for cuerda in lista_cuerdas:
        if cuerda["tension"] > mayor["tension"]:
            mayor = cuerda

    return mayor


def obtenerMenorFactor(lista_cuerdas):
    menor = lista_cuerdas[0]
    for cuerda in lista_cuerdas:
        if cuerda["factor_seguridad"] < menor["factor_seguridad"]:
            menor = cuerda

    return menor


def mostrarResumen(lista_cuerdas):
    print("\n=========== RESULTADOS ===========")
    for cuerda in lista_cuerdas:
        print()
        print("Cuerda:", cuerda["nombre"])
        print("Longitud:",round(cuerda["longitud"],3))
        print("Ángulo X:",round(cuerda["angulo_x"],2))
        print("Ángulo Y:",round(cuerda["angulo_y"],2))
        print("Ángulo Z:",round(cuerda["angulo_z"],2))
        print("Porcentaje:",round(cuerda["porcentaje"]*100,2),"%")
        print("Tensión:",round(cuerda["tension"],2),"N")
        print("Factor:",round(cuerda["factor_seguridad"],2))
        print("Estado:", "Correcto" if cuerda["viable"] else "No viable")
        print("-"*40)
from conexion import conectar
def obtenerResistenciaMaterial(id_material):
    conexion = conectar()
    if conexion is None:
        return None
    cursor = conexion.cursor()
    sql = """
    SELECT resistencia_maxima
    FROM materiales
    WHERE id_material=%s
    """

    cursor.execute(sql, (id_material,))

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    if resultado is None:

        return None

    return float(resultado[0])


def calcularFactores(lista_cuerdas):

    for cuerda in lista_cuerdas:

        resistencia = obtenerResistenciaMaterial(

            cuerda["id_material"]

        )

        cuerda["resistencia"] = resistencia

        if resistencia is None:

            cuerda["factor_seguridad"] = 0

            cuerda["viable"] = False

            continue

        if cuerda["tension"] == 0:

            cuerda["factor_seguridad"] = 999999

            cuerda["viable"] = True

            continue

        fs = resistencia / cuerda["tension"]

        cuerda["factor_seguridad"] = fs

        cuerda["viable"] = fs >= 3

    return lista_cuerdas


def generarConclusion(lista_cuerdas):

    sistema = True

    mayor = lista_cuerdas[0]

    menor = lista_cuerdas[0]

    for cuerda in lista_cuerdas:

        if not cuerda["viable"]:

            sistema = False

        if cuerda["tension"] > mayor["tension"]:

            mayor = cuerda

        if cuerda["factor_seguridad"] < menor["factor_seguridad"]:

            menor = cuerda

    return {

        "viable": sistema,

        "mayor_tension": mayor["nombre"],

        "tension_maxima": mayor["tension"],

        "menor_factor": menor["nombre"],

        "factor_minimo": menor["factor_seguridad"]

    }


def mostrarConclusion(conclusion):
    print("\n==============================")
    print("CONCLUSIÓN")
    print("==============================")
    print()
    if conclusion["viable"]:
        print("Sistema: VIABLE")
    else:
        print("Sistema: NO VIABLE")
    print()
    print("Mayor tensión:")
    print(conclusion["mayor_tension"])
    print(round(conclusion["tension_maxima"],2),"N")
    print()
    print("Menor factor de seguridad:")
    print(conclusion["menor_factor"])
    print(round(conclusion["factor_minimo"],2))


def realizarAnalisis(masa,lista_cuerdas,mostrar=True):

    peso = calcularPeso(masa)

    lista_cuerdas = calcularPorcentajes(lista_cuerdas)
    lista_cuerdas = calcularTensiones(lista_cuerdas,peso)
    lista_cuerdas = calcularFactores(lista_cuerdas)

    conclusion = generarConclusion(lista_cuerdas)

    if mostrar:

        mostrarResumen(lista_cuerdas)

        mostrarConclusion(conclusion)

    return (lista_cuerdas,conclusion)