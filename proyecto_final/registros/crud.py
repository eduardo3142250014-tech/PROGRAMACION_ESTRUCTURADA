from conexion import conectar

def insertar(nombre_proyecto,
              descripcion,
              peso_candelabro,
              x_candelabro,
              y_candelabro,
              z_candelabro,
              numero_cuerdas,
              resultado,
              factor_seguridad,
              viable,
              id_empleado):

    try:

        conexion = conectar()

        if conexion is None:
            return None

        cursor = conexion.cursor()

        sql = """
        INSERT INTO registros
        (
        nombre_proyecto,
        descripcion,
        peso_candelabro,
        x_candelabro,
        y_candelabro,
        z_candelabro,
        numero_cuerdas,
        resultado,
        factor_seguridad,
        viable,
        id_empleado
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        valores = (

            nombre_proyecto,

            descripcion,

            peso_candelabro,

            x_candelabro,

            y_candelabro,

            z_candelabro,

            numero_cuerdas,

            resultado,

            factor_seguridad,

            viable,

            id_empleado

        )

        cursor.execute(sql, valores)

        conexion.commit()

        id_registro = cursor.lastrowid

        cursor.close()
        conexion.close()

        return id_registro

    except Exception as err:

        print(f"\nError al insertar registro.\n{err}")

        return None

def buscar(id_registro):

    try:

        conexion = conectar()

        if conexion is None:
            return None

        cursor = conexion.cursor()

        sql = """
        SELECT *
        FROM registros
        WHERE id_registro=%s
        """

        cursor.execute(sql, (id_registro,))

        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        return registro

    except Exception as err:

        print(f"\nError al buscar registro.\n{err}")

        return None


def consultar():

    try:

        conexion = conectar()

        if conexion is None:
            return []

        cursor = conexion.cursor()

        cursor.execute("""
        SELECT *
        FROM registros
        ORDER BY id_registro
        """)

        registros = cursor.fetchall()

        cursor.close()
        conexion.close()

        return registros

    except Exception as err:

        print(f"\nError al consultar registros.\n{err}")

        return []


def actualizar(id_registro,
                nombre_proyecto,
                descripcion,
                peso_candelabro,
                x_candelabro,
                y_candelabro,
                z_candelabro,
                numero_cuerdas,
                resultado,
                factor_seguridad,
                viable,
                id_empleado):

    try:

        conexion = conectar()

        if conexion is None:
            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE registros

        SET

        nombre_proyecto=%s,

        descripcion=%s,

        peso_candelabro=%s,

        x_candelabro=%s,

        y_candelabro=%s,

        z_candelabro=%s,

        numero_cuerdas=%s,

        resultado=%s,

        factor_seguridad=%s,

        viable=%s,

        id_empleado=%s

        WHERE id_registro=%s
        """

        valores = (

            nombre_proyecto,

            descripcion,

            peso_candelabro,

            x_candelabro,

            y_candelabro,

            z_candelabro,

            numero_cuerdas,

            resultado,

            factor_seguridad,

            viable,

            id_empleado,

            id_registro

        )

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    except Exception as err:

        print(f"\nError al actualizar registro.\n{err}")

        return False


def eliminar(id_registro):

    try:

        conexion = conectar()

        if conexion is None:
            return False

        cursor = conexion.cursor()

        sql = """
        DELETE
        FROM registros
        WHERE id_registro=%s
        """

        cursor.execute(sql, (id_registro,))

        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    except Exception as err:

        print(f"\nError al eliminar registro.\n{err}")

        return False


def vaciar():

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        cursor.execute(

            "DELETE FROM cuerdas"

        )

        cursor.execute(

            "ALTER TABLE cuerdas AUTO_INCREMENT = 1"

        )

        cursor.execute(

            "DELETE FROM registros"

        )

        cursor.execute(

            "ALTER TABLE registros AUTO_INCREMENT = 1"

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al limpiar la tabla registros.\n{err}"

        )

        return False

def actualizarProyecto(id_registro,
                        nombre_proyecto):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE registros
        SET nombre_proyecto=%s
        WHERE id_registro=%s
        """

        cursor.execute(

            sql,

            (

                nombre_proyecto,

                id_registro

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al actualizar el proyecto.\n{err}"

        )

        return False


def actualizarDescripcion(id_registro,
                           descripcion):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE registros
        SET descripcion=%s
        WHERE id_registro=%s
        """

        cursor.execute(

            sql,

            (

                descripcion,

                id_registro

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al actualizar la descripción.\n{err}"

        )

        return False


def actualizarEmpleado(id_registro,
                        id_empleado):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE registros
        SET id_empleado=%s
        WHERE id_registro=%s
        """

        cursor.execute(

            sql,

            (

                id_empleado,

                id_registro

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al actualizar el empleado.\n{err}"

        )

        return False


def actualizarMasa(id_registro,
                    masa):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE registros
        SET peso_candelabro=%s
        WHERE id_registro=%s
        """

        cursor.execute(

            sql,

            (

                masa,

                id_registro

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al actualizar la masa.\n{err}"

        )

        return False


def actualizarPosicion(id_registro,
                        x,
                        y,
                        z):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE registros

        SET

        x_candelabro=%s,

        y_candelabro=%s,

        z_candelabro=%s

        WHERE id_registro=%s
        """

        cursor.execute(

            sql,

            (

                x,

                y,

                z,

                id_registro

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al actualizar la posición.\n{err}"

        )

        return False


def actualizarAnalisis(id_registro,
                        numero_cuerdas,
                        resultado,
                        factor_seguridad,
                        viable):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE registros

        SET

        numero_cuerdas=%s,

        resultado=%s,

        factor_seguridad=%s,

        viable=%s

        WHERE id_registro=%s
        """

        cursor.execute(

            sql,

            (

                numero_cuerdas,

                resultado,

                factor_seguridad,

                viable,

                id_registro

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al actualizar el análisis.\n{err}"

        )

        return False
def consultarCuerdas(id_registro):

    try:

        conexion = conectar()

        if conexion is None:

            return []

        cursor = conexion.cursor()

        sql = """
        SELECT *
        FROM cuerdas
        WHERE id_registro=%s
        ORDER BY id_cuerda
        """

        cursor.execute(

            sql,

            (

                id_registro,

            )

        )

        cuerdas = cursor.fetchall()

        cursor.close()

        conexion.close()

        return cuerdas

    except Exception as err:

        print(

            f"\nError al consultar las cuerdas.\n{err}"

        )

        return []


def buscarCuerda(id_cuerda):

    try:

        conexion = conectar()

        if conexion is None:

            return None

        cursor = conexion.cursor()

        sql = """
        SELECT *
        FROM cuerdas
        WHERE id_cuerda=%s
        """

        cursor.execute(

            sql,

            (

                id_cuerda,

            )

        )

        cuerda = cursor.fetchone()

        cursor.close()

        conexion.close()

        return cuerda

    except Exception as err:

        print(

            f"\nError al buscar la cuerda.\n{err}"

        )

        return None


def insertarCuerda(nombre,
                    x,
                    y,
                    z,
                    longitud,
                    angulo_x,
                    angulo_y,
                    angulo_z,
                    tension,
                    id_material,
                    id_registro):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        sql = """
        INSERT INTO cuerdas
        (
        nombre,
        x_anclaje,
        y_anclaje,
        z_anclaje,
        longitud,
        angulo_x,
        angulo_y,
        angulo_z,
        tension,
        id_material,
        id_registro
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        valores = (

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

        )

        cursor.execute(

            sql,

            valores

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al insertar la cuerda.\n{err}"

        )

        return False


def actualizarDatosCuerda(id_cuerda,
                           datos):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE cuerdas

        SET

        x_anclaje=%s,

        y_anclaje=%s,

        z_anclaje=%s,

        longitud=%s,

        angulo_x=%s,

        angulo_y=%s,

        angulo_z=%s,

        tension=%s,

        id_material=%s

        WHERE id_cuerda=%s
        """

        valores = (

            datos["x"],

            datos["y"],

            datos["z"],

            datos["longitud"],

            datos["angulo_x"],

            datos["angulo_y"],

            datos["angulo_z"],

            datos["tension"],

            datos["id_material"],

            id_cuerda

        )

        cursor.execute(

            sql,

            valores

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al actualizar la cuerda.\n{err}"

        )

        return False


def eliminarCuerda(id_cuerda):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        sql = """
        DELETE
        FROM cuerdas
        WHERE id_cuerda=%s
        """

        cursor.execute(

            sql,

            (

                id_cuerda,

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al eliminar la cuerda.\n{err}"

        )

        return False
def actualizarAnalisis(id_registro,
                        numero_cuerdas,
                        resultado,
                        factor_seguridad,
                        viable):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE registros

        SET

        numero_cuerdas=%s,

        resultado=%s,

        factor_seguridad=%s,

        viable=%s

        WHERE id_registro=%s
        """

        cursor.execute(

            sql,

            (

                numero_cuerdas,

                resultado,

                factor_seguridad,

                viable,

                id_registro

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al actualizar el análisis.\n{err}"

        )

        return False
def actualizarDatosCuerda(id_cuerda,
                           datos):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE cuerdas

        SET

        x_anclaje=%s,

        y_anclaje=%s,

        z_anclaje=%s,

        longitud=%s,

        angulo_x=%s,

        angulo_y=%s,

        angulo_z=%s,

        tension=%s,

        id_material=%s

        WHERE id_cuerda=%s
        """

        valores = (

            datos["x"],

            datos["y"],

            datos["z"],

            datos["longitud"],

            datos["angulo_x"],

            datos["angulo_y"],

            datos["angulo_z"],

            datos["tension"],

            datos["id_material"],

            id_cuerda

        )

        cursor.execute(

            sql,

            valores

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al actualizar la cuerda.\n{err}"

        )

        return False
def actualizarPosicionCuerda(id_cuerda,
                             x,
                             y,
                             z):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE cuerdas

        SET

        x_anclaje=%s,

        y_anclaje=%s,

        z_anclaje=%s

        WHERE id_cuerda=%s
        """

        cursor.execute(

            sql,

            (

                x,

                y,

                z,

                id_cuerda

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al actualizar la posición de la cuerda.\n{err}"

        )

        return False
def actualizarMaterialCuerda(id_cuerda,
                             id_material):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE cuerdas

        SET

        id_material=%s

        WHERE id_cuerda=%s
        """

        cursor.execute(

            sql,

            (

                id_material,

                id_cuerda

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al actualizar el material.\n{err}"

        )

        return False