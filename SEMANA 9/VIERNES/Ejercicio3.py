#SOLICITANDO DATOS
metros = int(input("Ingrese la cantidad de metros de alambre: "))

#RESOLVIENDO
Qmetros = metros//500
residuoQ = metros%500
Tmetros = residuoQ//300
residuoT = residuoQ%300
Smetro3 = residuoT//75
ultimoRollo = residuoT%75

print(f"{Qmetros} rollos de 500 metros")
print(f"{Tmetros} rollos de 300 metros")
print(f"{Smetros} rollos de 75 metros")
print(f"El ultimo rollo tendra {ultimoRollo} metro")
