import math as m

#SOLICITANDO DATOS
arista = int(input("Ingrese un valor para la arista: "))
nombrefigura = input("Ingrese nombre variable: ")

#RESOLVER LA FORMULA DEL AREA
area = round(arista**2 * m.sqrt(3), 3)

#RESOLVER LA FORMULA DEL VOLUMEN
volumen = round((m.sqrt(2)/12) * arista**3, 3)

print(f"Nombre figura: {nombrefigura}")
print(f"El area es: {area}")
print(f"El volumen es: {volumen}")