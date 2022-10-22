#SOLICITANDO DATOS
salarioMensual = float(input("Ingrese su salario mensual: "))
numeroPersonas = int(input("Ingrese el numero de personas a cargo: "))

#RESOLVIENDO
if numeroPersonas == 1:
    if 0 < salarioMensual <= 500:
        print("Tipo de linea al que puede acceder: P")
    elif salarioMensual > 500:
        print("Tipo de linea al que puede acceder: O")
elif 2 <= numeroPersonas <= 4:
    if 0 < salarioMensual <= 750:
        print("Tipo de linea al que puede acceder: P")
    elif salarioMensual > 750:
        print("Tipo de linea al que puede acceder: O")
else:
    if 0 < salarioMensual <= 1000:
        print("Tipo de linea al que puede acceder: P")
    elif salarioMensual > 1000:
        print("Tipo de linea al que puede acceder: O")