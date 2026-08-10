from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet

from reportes import datos
import funciones


def generar():

    funciones.titulo("GENERAR REPORTE PDF")

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

    documento = SimpleDocTemplate(
        f"Reporte_{id_registro}.pdf"
    )

    estilos = getSampleStyleSheet()

    contenido = []

    contenido.append(

        Paragraph(
            "<b>REPORTE DEL SISTEMA DE TENSIONES</b>",
            estilos["Title"]
        )

    )

    contenido.append(Spacer(1,20))

    etiquetas = [

        ("ID", registro[0]),

        ("Proyecto", registro[1]),

        ("Descripción", registro[2]),

        ("Peso", f"{registro[3]} kg"),

        ("Posición",
         f"({registro[4]}, {registro[5]}, {registro[6]})"),

        ("Número de cuerdas", registro[7]),

        ("Resultado", registro[8]),

        ("Factor de Seguridad", round(registro[9],2)),

        ("Viable",
         "SI" if registro[10] else "NO"),

        ("Fecha", registro[11]),

        ("Empleado", registro[12])

    ]

    for etiqueta, valor in etiquetas:

        contenido.append(

            Paragraph(

                f"<b>{etiqueta}:</b> {valor}",

                estilos["Normal"]

            )

        )

    contenido.append(Spacer(1,20))

    contenido.append(

        Paragraph(

            "<b>CUERDAS</b>",

            estilos["Heading2"]

        )

    )

    contador = 1

    for cuerda in cuerdas:

        contenido.append(Spacer(1,10))

        contenido.append(

            Paragraph(

                f"<b>Cuerda {contador}</b>",

                estilos["Heading3"]

            )

        )

        contenido.append(
            Paragraph(f"Nombre: {cuerda[0]}", estilos["Normal"])
        )

        contenido.append(
            Paragraph(f"Material: {cuerda[1]}", estilos["Normal"])
        )

        contenido.append(
            Paragraph(f"Longitud: {round(cuerda[2],3)} m", estilos["Normal"])
        )

        contenido.append(
            Paragraph(f"Ángulo X: {round(cuerda[3],2)}°", estilos["Normal"])
        )

        contenido.append(
            Paragraph(f"Ángulo Y: {round(cuerda[4],2)}°", estilos["Normal"])
        )

        contenido.append(
            Paragraph(f"Ángulo Z: {round(cuerda[5],2)}°", estilos["Normal"])
        )

        contenido.append(
            Paragraph(f"Tensión: {round(cuerda[6],2)} N", estilos["Normal"])
        )

        contenido.append(
            Paragraph(f"Resistencia: {round(cuerda[7],2)} N", estilos["Normal"])
        )

        fs = 0

        if cuerda[6] != 0:

            fs = cuerda[7] / cuerda[6]

        contenido.append(

            Paragraph(

                f"Factor de Seguridad: {round(fs,2)}",

                estilos["Normal"]

            )

        )

        contenido.append(

            Paragraph(

                f"Estado: {'CORRECTO' if fs>=3 else 'NO VIABLE'}",

                estilos["Normal"]

            )

        )

        contador += 1

    documento.build(contenido)

    print("\nReporte PDF generado correctamente.")

    print(f"\nArchivo: Reporte_{id_registro}.pdf")

    funciones.espereTecla()