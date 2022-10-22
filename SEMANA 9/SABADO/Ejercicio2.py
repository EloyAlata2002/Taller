import random as r

#GENERANDO DATOS
codigo = r.randint(1000, 9999)
hora = r.randint(1, 24)
minuto = r.randint(1, 60)
segundo = r.randint(1, 60)

print(f"El codigo generado es: {codigo}{hora}{minuto}{segundo}")
print(f"El codigo del trabajor es: {codigo}")
print(f"La hora de entrada del trabajor es: {hora}")
print(f"El minuto de entrada del trabajor es: {minuto}")
print(f"El segundo del trabajor es: {segundo}")