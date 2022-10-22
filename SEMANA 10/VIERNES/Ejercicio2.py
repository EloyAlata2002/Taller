#DEFINIENDO VALORES
transporte = " "
tiempo = -1
momento = 0
ruta = " "

contTA = 0
contTT = 0
contTP = 0

contM1 = 0
contM2 = 0
contM3 = 0
contM4 = 0

contRA = 0
contRB = 0
contRC = 0
contRO = 0

contTRA = 0
contTRB = 0
contTRC = 0
contTRO = 0

promedioA = 0
promedioB = 0
promedioC = 0
promedioO = 0

while transporte.upper() != "X":
    transporte = " "
    tiempo = -1
    momento = 0
    ruta = " "
    while transporte.upper() != "A" and transporte.upper() != "T" and transporte.upper() != "P" and transporte.upper() != "X":
        transporte = input("Medio de transporte (A: Auto propio; T: Privado (Taxi); P: Transporte público): ")
    if transporte.upper() != "X":
        while tiempo < 0:
            tiempo = int(input("Tiempo de duracion del viaje: "))
        while momento != 1 and momento != 2 and momento != 3 and momento != 4:
            momento = int(input("Momento del dia (1: Entre 7:00 y 9:00; 2: Entre 12:00 y 14:00; 3: Entre 17:00 y 19:00; 4: A partir de las 22:00): "))
        while ruta.upper() != "A" and ruta.upper() != "B" and ruta.upper() != "C" and ruta.upper() != "O":
            ruta = input("Ruta elegida (A: Av. Arequipa; B: Av. Brasil; C: Paseo de la República; O: Otra ruta): ")

    if transporte.upper() == "A":
        contTA += 1
    if transporte.upper() == "T":
        contTT += 1
    if transporte.upper() == "P":
        contTP += 1

    if momento == 1:
        contM1 += 1
    if momento == 2:
        contM2 += 1
    if momento == 3:
        contM3 += 1
    if momento == 4:
        contM4 += 1

    if ruta.upper() == "A":
        contRA += 1
        contTRA += tiempo
    if ruta.upper() == "B":
        contRB += 1
        contTRB += tiempo
    if ruta.upper() == "C":
        contRC += 1
        contTRC += tiempo
    if ruta.upper() == "O":
        contRO += 1
        contTRO += tiempo

print("REPORTE")

print("Cantidad de usuarios por medio de transporte: ")
print(f"Auto propio: {contTA}")
print(f"Privado: {contTT}")
print(f"Transporte publico: {contTP}")

if contM1 > contM2 and contM1 > contM3 and contM1 > contM4:
    print(f"Momentos con mayor cantidad de viajes son: {contM1}")
if contM2 > contM1 and contM2 > contM3 and contM2 > contM4:
    print(f"Momentos con mayor cantidad de viajes son: {contM2}")
if contM3 > contM2 and contM3 > contM1 and contM3 > contM4:
    print(f"Momentos con mayor cantidad de viajes son: {contM3}")
if contM4 > contM2 and contM4 > contM3 and contM4 > contM1:
    print(f"Momentos con mayor cantidad de viajes son: {contM1}")
if contM1 >= contM2 >= contM3 >= contM4:
    print(f"Momentos con mayor cantidad de viajes son: {contM1}, {contM2}, {contM3}, {contM4}")

print("Tiempo promedio de viaje por ruta son: ")
if contTRA > 0:
    promedioA = contTRA / contRA
if contTRB > 0:
    promedioB = contTRB / contRB
if contTRC > 0:
    promedioC = contTRC / contRC
if contTRO > 0:
    promedioO = contRO / contTRO
print(f"Av. Arequipa: {promedioA}")
print(f"Av. Brasil: {promedioB}")
print(f"Paseo de la Republica: {promedioC}")
print(f"Otra ruta: {promedioO}")