# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).
def borrarPantalla():
    print("\033c")

def funcion1():
    nombre=input("Nombre: ").upper().strip()
    apellido=input("Apellidos: ").upper().strip()
    print(f"El nombre del alumno es: {nombre} {apellido}")

def funcion3(nom, ape):
    nombre=nom
    apellido=ape 
    print(f"El nombre del alumno es: {nombre} {apellido}")


def funcion2():
    nombre=input("Nombre: ").upper().strip()
    apellido=input("Apellidos: ").upper().strip()
    return nombre,apellido

def funcion4(nom, ape):
    nombre=nom
    apellido=ape 
    return nombre,apellido
