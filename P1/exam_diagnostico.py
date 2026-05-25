def ventaAutos():
    #entrada
   
    impuesto = 0
    total = 0
    ops = "S"
    autos = 1
    acum_pv = 0

    #proceso
    while ops == "S":
        marca = input("Marca: ").strip().upper()
        origen = input("Origen: ").strip().upper()
        costo = float(input("Costo: "))
    

        if(origen == "ALEMANIA"):
            impuesto = 0.2
            
        elif(origen == "JAPON"):
            impuesto = 0.3

        elif(origen == "ITALIA"):
            impuesto = 0.15

        elif(origen == "USA"):
            impuesto = 0.08    

        impuesto_pesos = costo * impuesto
        total = costo + impuesto_pesos 
        ops = input("Desea ingresar otro carro? (S/N): ").strip().upper()
    #salida

   
def borrarPantalla():
    print("\033C")

    
ventaAutos()