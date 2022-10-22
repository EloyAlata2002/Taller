#EJERCICIO 1
#REALIZANDO FUNCIONES
def hallarFactorial(i):
    fact = 1 #LE ASIGNO 1 PORQUE EL FACTORIAL COMIENZA A MULTIPLICAR DESDE EL 1
    for j in range(1, i + 1): #j IRA ITERANDO DESDE 1 HASTA EL VALOR i + 1, HAGO ESO PARA QUE TOME EL RECORRIDO COMPLETO
        fact = fact * j 
    return fact

#DEFINIENDO VARIABLE
n = -1
e = 0.0
factorial = 0.0

#VALIDANDO VARIABLE
while n < 0 or n > 121:
    n = int(input("Ingrese el valor de N: "))

#RESOLVIENDO
for i in range(1, n + 1): #i IRA ITERANDO DESDE 1 HASTA EL VALOR n + 1, HAGO ESO PARA QUE TOME EL RECORRIDO COMPLETO
    factorial = hallarFactorial(i) #A UNA VARIABLE FACTORIAL LE ASIGNO EL VALOR OBTENIDO DE LA FUNCION
    e += (i**2)/(2*(factorial)) #SE REALIZA LA SUMATORIA PARA HALLAR e

print(f"El valor del numero e es: {round(e,5)}") #CON round(e,5) ESTOY REDONDEANDO A 5 DECIMALES