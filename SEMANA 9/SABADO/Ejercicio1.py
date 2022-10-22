import math as m

#SOLICITANDO DATOS
a = int(input("Ingrese la arista: "))

#RESOLVER FORMULA DEL AREA
area = round(a**2 * m.sqrt(3), 7)

#RESOLVER FORMULA DEL VOLUMEN
volumen = round((m.sqrt(2)/12) * a**3, 3)

print(f"El area del tetraedro es: {area}")
print(f"El volumen del tetraedro es: {volumen}")