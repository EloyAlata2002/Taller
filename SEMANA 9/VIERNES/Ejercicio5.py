#SOLICITANDO DATOS
salarioMensual = float(input("Ingrese el salario mensual: "))
numeroPersona = int(input("Ingrese el numero de personas a cargo: "))

if numeroPersona == 1:
    if  0 < salarioMensual <= 500:
        print("Tipo de linea al que puede acceder: P")
    elif salarioMensual > 500:
        print("Tipo de linea al que puede acceder: O")
elif 2 <= numeroPersona <= 4:
    if 0 < salarioMensual <= 750:
        print("Tipo de linea al que puede acceder: P")
    elif salarioMensual > 750:
        print("Tipo de linea al que puede acceder: O")
else:
    if 0 < salarioMensual <= 1000:
        print("Tipo de linea al que puede acceder: P")
    elif salarioMensual > 1000:
        print("Tipo de linea al que puede acceder: O")