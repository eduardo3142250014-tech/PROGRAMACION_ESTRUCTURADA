'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''
'''
print("\033c")

num_tab = int(input("Dame un numero para obtener la tabla de multiplicar: "))

num = 1

multi = num_tab * num
print(f"{num_tab} X {num} = {multi}")
num += 1

multi = num_tab * num
print(f"{num_tab} X {num} = {multi}")
num += 1

multi = num_tab * num
print(f"{num_tab} X {num} = {multi}")
num += 1

multi = num_tab * num
print(f"{num_tab} X {num} = {multi}")
num += 1

multi = num_tab * num
print(f"{num_tab} X {num} = {multi}")
num += 1

multi = num_tab * num
print(f"{num_tab} X {num} = {multi}")
num += 1

multi = num_tab * num
print(f"{num_tab} X {num} = {multi}")
num += 1

multi = num_tab * num
print(f"{num_tab} X {num} = {multi}")
num += 1

multi = num_tab * num
print(f"{num_tab} X {num} = {multi}")
num += 1

multi = num_tab * num
print(f"{num_tab} X {num} = {multi}")
num += 1
'''


'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con estructuras de control
  2.- Sin funciones

'''
'''
#print("\033c")
num_tab = int(input("Dame un numero para obtener la tabla de multiplicar: "))
for num in range(1, 11):
    multi = num_tab * num
    print(f"{num_tab} X {num} = {multi} ")
    num += 1
'''   

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con decrementos de 10 
  2.- Sin funciones

'''
'''
num_tab = int(input("Dame un numero para obtener la tabla de multiplicar: "))
for i in range(100,0,-10):
    multi = num_tab * i
    print(f"{num_tab} X {i} = {multi} ")
    i += 1
'''    
    
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con decrementos de 10 
  2.- Sin funciones

'''
'''
cont = 100
num_tab = int(input("Dame un numero para obtener la tabla de multiplicar: "))

while cont >= 10:
    multi = num_tab * cont
    print(f"{num_tab} X {cont} = {multi} ")
    cont -= 10
'''
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- con funciones

'''
'''
def tablas(num_tab, n):
    
    mul = num_tab * n
    print(f"{num_tab} X {n} = {mul}")
    n += 1
    return n


num_tab = int(input("Dame un numero para obtener la tabla de multiplicar: "))
num = 1

num = tablas(num_tab,num)
num = tablas(num_tab,num)
num = tablas(num_tab,num)
num = tablas(num_tab,num)
num = tablas(num_tab,num)
num = tablas(num_tab,num)
num = tablas(num_tab,num)
num = tablas(num_tab,num)
num = tablas(num_tab,num)
num = tablas(num_tab,num)
'''
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con estructuras de control
  2.- con funciones

'''
def tablas(num_tab, n):
    
    mul = num_tab * n
    print(f"{num_tab} X {n} = {mul}")
    n += 1
    return n


num_tab = int(input("Dame un numero para obtener la tabla de multiplicar: "))
num = 1

for i in range(1,11):
  num = tablas(num_tab,num)
