#SOLICITANDO DATOS
codigo = int(input("Ingrese el codigo del producto: "))
unidades = int(input("Ingrese la cantidad de unidades: "))

#RESOLVIENDO
if codigo == 1:
    montoPagar = unidades * 15.75
elif codigo == 2:
    montoPagar = unidades * 21
elif codigo == 3:
    montoPagar = unidades * 8.5
elif codigo == 4:
    montoPagar = unidades * 25
elif codigo == 5:
    montoPagar = unidades * 13.25

if montoPagar < 100:
    print("El cliente no aplica para el descuento")
    print(f"El monto a pagar es: {montoPagar}")
elif montoPagar >= 100:
    descuento = montoPagar * 0.11
    montoFinal = montoPagar - descuento
    print(f"El cliente aplica para un descuento de 11% y es: {descuento}")
    print(f"El monto a pagar es: {montoFinal}")