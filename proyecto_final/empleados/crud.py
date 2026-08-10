from conexion import conectar

def existe(id_empleado):

    return buscar(id_empleado) is not None

def insertar(nombre,
              apellido_paterno,
              apellido_materno,
              telefono,
              correo,
              puesto):

    try:

        conexion = conectar()

        if conexion is None:
            return False

        cursor = conexion.cursor()

        sql = """
        INSERT INTO empleados
        (
        nombre,
        apellido_paterno,
        apellido_materno,
        telefono,
        correo,
        puesto
        )
        VALUES
        (%s,%s,%s,%s,%s,%s)
        """

        valores = (
            nombre,
            apellido_paterno,
            apellido_materno,
            telefono,
            correo,
            puesto
        )

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    except Exception as err:

        print(f"\nError al insertar empleado.\n{err}")

        return False


def buscar(id_empleado):

    try:

        conexion = conectar()

        if conexion is None:
            return None

        cursor = conexion.cursor()

        sql = """
        SELECT *
        FROM empleados
        WHERE id_empleado=%s
        """

        cursor.execute(sql, (id_empleado,))

        empleado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return empleado

    except Exception as err:

        print(f"\nError al buscar empleado.\n{err}")

        return None


def consultar():

    try:

        conexion = conectar()

        if conexion is None:
            return []

        cursor = conexion.cursor()

        cursor.execute("""
        SELECT *
        FROM empleados
        ORDER BY id_empleado
        """)

        empleados = cursor.fetchall()

        cursor.close()
        conexion.close()

        return empleados

    except Exception as err:

        print(f"\nError al consultar empleados.\n{err}")

        return []


def actualizar(id_empleado,
                nombre,
                apellido_paterno,
                apellido_materno,
                telefono,
                correo,
                puesto):

    try:

        conexion = conectar()

        if conexion is None:
            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE empleados

        SET

        nombre=%s,

        apellido_paterno=%s,

        apellido_materno=%s,

        telefono=%s,

        correo=%s,

        puesto=%s

        WHERE id_empleado=%s
        """

        valores = (

            nombre,

            apellido_paterno,

            apellido_materno,

            telefono,

            correo,

            puesto,

            id_empleado

        )

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    except Exception as err:

        print(f"\nError al actualizar empleado.\n{err}")

        return False


def eliminar(id_empleado):

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        cursor.execute(

            """
            SELECT id_registro
            FROM registros
            WHERE id_empleado=%s
            """,

            (id_empleado,)

        )

        registros = cursor.fetchall()

        for registro in registros:

            cursor.execute(

                """
                DELETE
                FROM cuerdas
                WHERE id_registro=%s
                """,

                (registro[0],)

            )

        cursor.execute(

            """
            DELETE
            FROM registros
            WHERE id_empleado=%s
            """,

            (id_empleado,)

        )

        cursor.execute(

            """
            DELETE
            FROM empleados
            WHERE id_empleado=%s
            """,

            (id_empleado,)

        )

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al eliminar empleado.\n{err}"

        )

        return False


def vaciar():

    try:

        conexion = conectar()

        if conexion is None:

            return False

        cursor = conexion.cursor()

        cursor.execute("""

        DELETE FROM cuerdas

        """)

        cursor.execute("""

        ALTER TABLE cuerdas AUTO_INCREMENT = 1

        """)

        cursor.execute("""

        DELETE FROM registros

        """)

        cursor.execute("""

        ALTER TABLE registros AUTO_INCREMENT = 1

        """)

        cursor.execute("""

        DELETE FROM empleados

        """)

        cursor.execute("""

        ALTER TABLE empleados AUTO_INCREMENT = 1

        """)

        conexion.commit()

        cursor.close()

        conexion.close()

        return True

    except Exception as err:

        print(

            f"\nError al limpiar la tabla empleados.\n{err}"

        )

        return False