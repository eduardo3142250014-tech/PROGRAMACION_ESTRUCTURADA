"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""


#Funciones más comunes en las listas}

paises=["mexica","Canada","EUA","mexico","Brasil"]
numeros=[23,45,8,28]
varios=[33,3.1416,"hola",True]
vacio=[] 
 



#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacio)


#Recorrer la lista 
#1er forma 
valores=[]
paises=["mexico","canada","EUA","mexico","Brasil"]
for i in paises:
    valores.append(i)
    print(i)
    print(valores)

# #2do forma 
paises=["mexico","canada","EUA","mexico","Brasil"]


for i in range(0,len(paises)):
    print(paises[i])
    print(i)



#ordenar elementos de una lista

print(paises)
paises.sort()
print(paises)


#dar la vuelta a una lista
paises.reverse()
print(paises)




#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises=["mexica","Canada","EUA","mexico","Brasil"]
paises.append("honduras")
print(paises)


#2da forma

paises.insert(1,"cuba")
print(paises)
paises.insert(8,"polonia")
print(paises)


#Eliminar, borrar, suprimir, un elemento de una lista
paises=["mexica","Canada","EUA","mexico","Brasil"]
print(paises)

#1er forma

paises.pop(3)
print(paises)




#2da forma 

paises.remove("EUA")
print(paises)


#Buscar un elemento dentro de la lista

encontro="mexica" in paises
print(encontro)


#Contar el numeros de veces que aparece un elemento dentro de una lista
numeros=[23,45,8,24,23,23,100]
paises=["mexico","Canada","EUA","mexico","Brasil"]

num_veces=numeros.count(23)
print(f"el valor 23 aparece {num_veces} veces en la lista numeros")

num_veces=paises.count("mexico")
print(f"el valor mexico aparece {num_veces} veces en la lista paises") 



#Conocer la posicion o indice en el que se encuentra un elemento de la lista

paises=["mexico","Canada","EUA","mexico","Brasil"]

posicion=paises.index("mexico")
print(f"encontre el valor en la posicion {posicion} de la lista paises")


for i in range(0,len(paises)):

    if paises[i]=="mexico":
        posicion=i
        print(f"encontre el valor en la posicion {posicion} de la lista paises") 



#Unir el contenido de una lista dentro de otra lista

numeros1=[23,45,8,24,23,23,100]
numeros2=[100,-100]
print(numeros1)
print(numeros2)

numeros1.extend(numeros2)

print(numeros1)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente

numeros1.sort()
numeros1.reverse()
print(numeros1)



