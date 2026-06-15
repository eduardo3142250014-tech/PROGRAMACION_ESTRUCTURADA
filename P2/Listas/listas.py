print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

numeros=[23,45,8,24,0,100]
print(numeros)

lista=""
for i in numeros:
    lista+=str(i)+","
print("[" + lista + "]")




lista=""
for i in range(0,len(numeros)):
    lista+=f"{numeros[i]},"
print("[" + lista + "]")

numeros=[23,45,8,24,0,100]
lista=""
for i in range(0,len(numeros)):
    lista+=f"{numeros[i]},"
print("[" + lista + "]")

i=0
lista=""
while i<len(numeros):
    lista+=f"{numeros[i]},"
    i+=1
print("[" + lista + "]")



#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

#primer forma:
palabras=["UTD","tercer","cuatrimestre","TI"]
buscar=input("ingresa la palabra a buscar: ")


if buscar in palabras:
    print( f"encontre la palabra {buscar} en la lista palabras" )
else:    print( f"no encontre la palabra {buscar} en la lista palabras" )

    




#2DA FORMA
 
palabras=["UTD","tercer","cuatrimestre","TI"]
buscar=input("ingresa la palabra a buscar: ").strip()

encontro=False
for i in palabras:
    if i==buscar:
        encontro=True        
if encontro==True:
    print( f"encontre la palabra {buscar} en la lista palabras" )
elif encontro==False:   
    print( f"no encontre la palabra {buscar} en la lista palabras" )       

#3er FORMA este con len y range

for i in range(len(palabras)):
    if palabras[i]==buscar:
        encontro=True
    else:
        encontro=False
if encontro==True:
    print( f"encontre la palabra {buscar} en la lista palabras" )
elif encontro==False:   
    print( f"no encontre la palabra {buscar} en la lista palabras" )

    

#forma while
i=0
encontro=False
while i<len(palabras):
    if palabras[i]==buscar:
        encontro=True
    i+=1
if encontro==True:
    print( f"encontre la palabra {buscar} en la lista palabras" )
elif encontro==False:   
    print( f"no encontre la palabra {buscar} en la lista palabras" )

#Ejemplo 3 Añadir elementos a la lista

lista.append(input("Ingresa un valor").strip())
lista=[]
#opcion 1
true=True
while true:
    valor=input("Ingresa un valor").strip()
    lista.append(valor) 
    true=input("Ingresa false o true para continuar: ").strip
    if true=="false":
        true=False

#opcion 2

opc="true"
while opc=="true":
    valor=input("Ingresa un valor").strip()
    lista.append(valor) 
    opc=input("quieres agregar otro valor true o false?").lower().strip()
print(lista)

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda =[
    ["Carlos","6181234567"],
    ["Adrian","6182332456"],
    ["Luis","6182223444"]
]
print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])
elemento=""
for r in range(0,3): 
    for c in range(0,2):
            elemento+=f"{agenda[r][c]}, "
    elemento+="\n"
print(elemento)




