from conexion import conectar


def obtenerReporte(id_registro):

    conexion = conectar()

    if conexion is None:

        return None

    cursor = conexion.cursor()

    sql = """
    SELECT
        r.id_registro,
        r.nombre_proyecto,
        r.descripcion,
        r.peso_candelabro,
        r.x_candelabro,
        r.y_candelabro,
        r.z_candelabro,
        r.numero_cuerdas,
        r.resultado,
        r.factor_seguridad,
        r.viable,
        r.fecha,
        CONCAT(

    e.nombre,

    ' ',

    e.apellido_paterno,

    ' ',

    e.apellido_materno

)
    FROM registros r

    INNER JOIN empleados e

    ON r.id_empleado=e.id_empleado

    WHERE r.id_registro=%s
    """

    cursor.execute(

        sql,

        (id_registro,)

    )

    registro = cursor.fetchone()

    if registro is None:

        cursor.close()

        conexion.close()

        return None

    sql = """
    SELECT

        c.nombre,

        m.nombre,

        c.longitud,

        c.angulo_x,

        c.angulo_y,

        c.angulo_z,

        c.tension,

        m.resistencia_maxima

    FROM cuerdas c

    INNER JOIN materiales m

    ON c.id_material=m.id_material

    WHERE c.id_registro=%s

    ORDER BY c.id_cuerda
    """

    cursor.execute(

        sql,

        (id_registro,)

    )

    cuerdas = cursor.fetchall()

    cursor.close()

    conexion.close()

    return {"registro": registro,"cuerdas": cuerdas}