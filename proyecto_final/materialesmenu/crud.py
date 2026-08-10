from conexion import conectar


def agregar(nombre, resistencia_maxima, descripcion):

    try:

        conexion = conectar()

        if conexion is None:
            return False

        cursor = conexion.cursor()

        sql = "INSERT INTO materiales (nombre, resistencia_maxima, descripcion) VALUES (%s, %s, %s)"

        valores = (nombre, resistencia_maxima, descripcion)

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    except Exception as err:

        print(f"\nError al agregar el material.\n{err}")

        return False


def buscar(id_material):

    try:

        conexion = conectar()

        if conexion is None:
            return None

        cursor = conexion.cursor()

        sql = "SELECT * FROM materiales WHERE id_material=%s"

        cursor.execute(sql, (id_material,))

        material = cursor.fetchone()

        cursor.close()
        conexion.close()

        return material

    except Exception as err:

        print(f"\nError al buscar el material.\n{err}")

        return None


def consultar():

    try:

        conexion = conectar()

        if conexion is None:
            return []

        cursor = conexion.cursor()

        sql = "SELECT * FROM materiales ORDER BY id_material"

        cursor.execute(sql)

        materiales = cursor.fetchall()

        cursor.close()
        conexion.close()

        return materiales

    except Exception as err:

        print(f"\nError al consultar los materiales.\n{err}")

        return []


def modificar(id_material, nombre, descripcion, resistencia_maxima):

    try:

        conexion = conectar()

        if conexion is None:
            return False

        cursor = conexion.cursor()

        sql = "UPDATE materiales SET nombre=%s, descripcion=%s, resistencia_maxima=%s WHERE id_material=%s"

        valores = (nombre, descripcion, resistencia_maxima, id_material)

        cursor.execute(sql, valores)

        sql = "SELECT id_registro FROM cuerdas WHERE id_material=%s"

        cursor.execute(sql, (id_material,))

        resultados = cursor.fetchall()

        registros = []

        for resultado in resultados:

            id_registro = resultado[0]

            if id_registro not in registros:

                registros.append(id_registro)

        conexion.commit()

        cursor.close()
        conexion.close()

        return registros

    except Exception as err:

        print(f"\nError al modificar el material.\n{err}")

        return False


def eliminar(id_material):

    try:

        conexion = conectar()

        if conexion is None:
            return False

        cursor = conexion.cursor()

        sql = "SELECT id_registro FROM cuerdas WHERE id_material=%s"

        cursor.execute(sql, (id_material,))

        resultados = cursor.fetchall()

        registros = []

        for resultado in resultados:

            id_registro = resultado[0]

            if id_registro not in registros:

                registros.append(id_registro)

        for id_registro in registros:

            sql = "DELETE FROM cuerdas WHERE id_registro=%s"

            cursor.execute(sql, (id_registro,))

            sql = "DELETE FROM registros WHERE id_registro=%s"

            cursor.execute(sql, (id_registro,))

        sql = "DELETE FROM materiales WHERE id_material=%s"

        cursor.execute(sql, (id_material,))

        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    except Exception as err:

        print(f"\nError al eliminar el material.\n{err}")

        return False


def vaciar():

    try:

        conexion = conectar()

        if conexion is None:
            return False

        cursor = conexion.cursor()

        cursor.execute("DELETE FROM cuerdas")

        cursor.execute("DELETE FROM registros")

        cursor.execute("DELETE FROM materiales")

        cursor.execute("ALTER TABLE cuerdas AUTO_INCREMENT = 1")

        cursor.execute("ALTER TABLE registros AUTO_INCREMENT = 1")

        cursor.execute("ALTER TABLE materiales AUTO_INCREMENT = 1")

        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    except Exception as err:

        print(f"\nError al limpiar las tablas relacionadas con materiales.\n{err}")

        return False