#SOLICITANDO DATOS
codigo = int(input("Ingrese el codigo del producto: "))
unidades = int(input("Ingrese la cantidad de unidades: "))

if codigo == 1:
    precioFinal = unidades * 15.75
elif codigo == 2:
    precioFinal = unidades * 21
elif codigo == 3:
    precioFinal = unidades * 8.5
elif codigo == 4:
    precioFinal = unidades * 25
elif codigo == 5:
    precioFinal = unidades * 13.25

if precioFinal < 100:
    print("El cliente no aplica para el descuento")
    print(f"El monto a pagar es: {precioFinal}")
elif precioFinal >= 100:
    descuento = precioFinal*0.11
    montoPagar = precioFinal-descuento
    print(f"El usuario aplica para el descuento de 11% este es: {descuento}")
    print(f"El monto a pagar es: {montoPagar}")