from conexion import conectar


def insertar(nombre,
              x_anclaje,
              y_anclaje,
              z_anclaje,
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

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    except Exception as err:

        print(f"\nError al insertar la cuerda.\n{err}")

        return False


def buscar(id_cuerda):

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

        cursor.execute(sql, (id_cuerda,))

        cuerda = cursor.fetchone()

        cursor.close()
        conexion.close()

        return cuerda

    except Exception as err:

        print(f"\nError al buscar la cuerda.\n{err}")

        return None


def consultar():

    try:

        conexion = conectar()

        if conexion is None:
            return []

        cursor = conexion.cursor()

        cursor.execute("""
        SELECT *
        FROM cuerdas
        ORDER BY id_cuerda
        """)

        cuerdas = cursor.fetchall()

        cursor.close()
        conexion.close()

        return cuerdas

    except Exception as err:

        print(f"\nError al consultar las cuerdas.\n{err}")

        return []


def actualizar(id_cuerda,
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
                id_registro):

    try:

        conexion = conectar()

        if conexion is None:
            return False

        cursor = conexion.cursor()

        sql = """
        UPDATE cuerdas

        SET

        nombre=%s,

        x_anclaje=%s,

        y_anclaje=%s,

        z_anclaje=%s,

        longitud=%s,

        angulo_x=%s,

        angulo_y=%s,

        angulo_z=%s,

        tension=%s,

        id_material=%s,

        id_registro=%s

        WHERE id_cuerda=%s
        """

        valores = (

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

            id_registro,

            id_cuerda

        )

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    except Exception as err:

        print(f"\nError al actualizar la cuerda.\n{err}")

        return False


def eliminar(id_cuerda):

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

        cursor.execute(sql, (id_cuerda,))

        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    except Exception as err:

        print(f"\nError al eliminar la cuerda.\n{err}")

        return False


def vaciar():

    try:

        conexion = conectar()

        if conexion is None:
            return False

        cursor = conexion.cursor()

        cursor.execute("""
        TRUNCATE TABLE cuerdas
        """)

        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    except Exception as err:

        print(f"\nError al limpiar la tabla cuerdas.\n{err}")

        return False