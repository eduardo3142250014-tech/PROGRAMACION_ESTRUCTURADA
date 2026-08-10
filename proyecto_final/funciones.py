import os
import re
import time

from config import COLORES
from config import ANCHO


def borrarPantalla():

    print("\033c")


def espereTecla():

    input("\nPresione ENTER para continuar...")


def centrar(texto):
    return texto.center(ANCHO)


def imprimirLento(texto, velocidad=0.03):

    for letra in texto:

        print(letra, end="", flush=True)

        time.sleep(velocidad)

    print()


def titulo(texto):

    borrarPantalla()

    print(COLORES["CYAN"])

    print("=" * ANCHO)

    print(centrar(texto))

    print("=" * ANCHO)

    print(COLORES["RESET"])


def confirmar(mensaje):

    opc = True
    while opc == True:

        respuesta = input(f"\n{mensaje} (S/N): ").upper().strip()

        if respuesta == "S":
            return True

        elif respuesta == "N":
            return False

        else:
            print("Respuesta inválida.")


def leerEntero(mensaje):
    opc = True
    while opc:

        try:

            numero = int(input(mensaje))
            opc == False
            return numero

        except ValueError:

            print("Ingrese un número entero válido.")


def leerFloat(mensaje):
    opc = True
    while opc:

        try:

            numero = float(input(mensaje))

            return numero

        except ValueError:

            print("Ingrese un número válido.")


def validarCorreo(correo):

    patron = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    return re.match(patron, correo)


def validarTelefono(telefono):

    patron = r'^[0-9]{10}$'

    return re.match(patron, telefono)


def validarTexto(texto):

    patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$'

    return re.match(patron, texto)


def accionExitosa():

    print(COLORES["VERDE"])

    print("\nAcción realizada correctamente.")

    print(COLORES["RESET"])

    espereTecla()


def accionFallida():

    print(COLORES["ROJO"])

    print("\nNo fue posible realizar la acción.")

    print(COLORES["RESET"])

    espereTecla()


def opcionInvalida():

    print(COLORES["AMARILLO"])

    print("\nOpción inválida.")

    print(COLORES["RESET"])

    espereTecla()