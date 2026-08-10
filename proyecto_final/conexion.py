import mysql.connector


def conectar():

    try:

        conexion = mysql.connector.connect(

            host="localhost",
            user="root",
            password="",
            database="sistema_tensiones"

        )

        return conexion

    except mysql.connector.Error as err:

        print(f"\nError al conectar con la base de datos.\n{err}")

        return None