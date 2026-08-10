from conexion import conectar


def obtenerMateriales():

    conexion = conectar()

    if conexion is None:
        return []

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM materiales")

    materiales = cursor.fetchall()

    cursor.close()
    conexion.close()

    return materiales


def mostrarMateriales():

    materiales = obtenerMateriales()

    print("\n======= MATERIALES =======\n")

    for material in materiales:

        print(f"{material[0]}. {material[1]} ({material[2]} N)")


def existe(id_material):

    materiales = obtenerMateriales()

    existe = False

    for material in materiales:

        if material[0] == id_material:

            existe = True

    return existe


def cantidad():

    return len(obtenerMateriales())