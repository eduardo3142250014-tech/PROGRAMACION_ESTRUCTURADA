"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""

print("\033c")

paises1 = ("México","Canada","EUA")

print(paises1)

varios =("Hola",True,33,3.1416)


print(paises1)
print(varios)

for i in paises1:
    print(i)

for i in range(0,len(paises1)):
    print(paises1[i])

i=0
while i<len(paises1):
    print(paises1[i])
    i+=1


print(f"El pais que inagura la copa del mundo 2026 es: {paises1[0]}")

edades = (23,24,18,20,20,23,24,19,24)

cuantos = edades.count(24)
print(cuantos)

#crear un programa que lea un numero y me diga en que posiciones se esncuentra



buscar=float(input("Ingrese el numero que quiere buscar"))
""" posiciones=edades.index(buscar) """#solo trae la primer posicion al momento de encontrar el valor
posiciones=[]
for i in range(0,len(edades)):
     if buscar==edades[i]:
       print(f"encontre el numero {buscar} en la posicion {i}")
       posiciones.append(i)



posiciones=tuple(posiciones)



#utilizando sets

buscar=float(input("Ingrese el numero que quiere buscar"))
""" posiciones=edades.index(buscar) """#solo trae la primer posicion al momento de encontrar el valor
posiciones={""}
posiciones.clear()
for i in range(0,len(edades)):
     if buscar==edades[i]:
       print(f"encontre el numero {buscar} en la posicion {i}")
       posiciones.add(i)



posiciones=tuple(posiciones)




      
