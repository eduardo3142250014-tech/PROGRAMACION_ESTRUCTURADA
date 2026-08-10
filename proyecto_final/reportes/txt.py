from reportes import datos
import funciones


def generar():

    funciones.titulo("GENERAR REPORTE TXT")

    id_registro = funciones.leerEntero(
        "Ingrese el ID del registro: "
    )

    reporte = datos.obtenerReporte(
        id_registro
    )

    if reporte is None:

        print("\nNo existe ese registro.")

        funciones.espereTecla()

        return

    registro = reporte["registro"]
    cuerdas = reporte["cuerdas"]

    archivo = open(

        f"Reporte_{id_registro}.txt",

        "w",

        encoding="utf-8"

    )

    archivo.write("="*70+"\n")
    archivo.write("       REPORTE DEL SISTEMA DE TENSIONES\n")
    archivo.write("="*70+"\n\n")

    archivo.write(f"ID Registro: {registro[0]}\n")
    archivo.write(f"Proyecto: {registro[1]}\n")
    archivo.write(f"Descripción: {registro[2]}\n")
    archivo.write(f"Peso: {registro[3]} kg\n")
    archivo.write(
        f"Posición: ({registro[4]}, {registro[5]}, {registro[6]})\n"
    )
    archivo.write(f"Número de cuerdas: {registro[7]}\n")
    archivo.write(f"Resultado: {registro[8]}\n")
    archivo.write(f"Factor de Seguridad: {round(registro[9],2)}\n")
    archivo.write(
        f"Viable: {'SI' if registro[10] else 'NO'}\n"
    )
    archivo.write(f"Fecha: {registro[11]}\n")
    archivo.write(f"Empleado: {registro[12]}\n\n")

    archivo.write("="*70+"\n")
    archivo.write("CUERDAS\n")
    archivo.write("="*70+"\n\n")

    contador = 1

    for cuerda in cuerdas:

        archivo.write(f"Cuerda {contador}\n")
        archivo.write(f"Nombre: {cuerda[0]}\n")
        archivo.write(f"Material: {cuerda[1]}\n")
        archivo.write(f"Longitud: {round(cuerda[2],3)} m\n")
        archivo.write(f"Ángulo X: {round(cuerda[3],2)}°\n")
        archivo.write(f"Ángulo Y: {round(cuerda[4],2)}°\n")
        archivo.write(f"Ángulo Z: {round(cuerda[5],2)}°\n")
        archivo.write(f"Tensión: {round(cuerda[6],2)} N\n")
        archivo.write(f"Resistencia: {round(cuerda[7],2)} N\n")

        fs = 0

        if cuerda[6] != 0:

            fs = cuerda[7] / cuerda[6]

        archivo.write(
            f"Factor de Seguridad: {round(fs,2)}\n"
        )

        archivo.write(

            f"Estado: {'CORRECTO' if fs>=3 else 'NO VIABLE'}\n\n"

        )

        contador += 1

    archivo.write("="*70+"\n")
    archivo.write("FIN DEL REPORTE\n")
    archivo.write("="*70+"\n")

    archivo.close()

    print("\nReporte generado correctamente.")

    print(f"\nArchivo: Reporte_{id_registro}.txt")

    funciones.espereTecla()