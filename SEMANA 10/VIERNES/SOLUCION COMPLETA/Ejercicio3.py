#DEFINIENDO VARIABLES
n = -1
b = -1
divisor = 4
s = 0.0
#VALIDANDO DATOS
while n < 0:
    n = int(input("Ingrese el valor de N: "))

while b < 0 or b > 6:
    b = float(input("ingrese el valor de b: "))

#RESOLVIENDO
for i in range(1, n + 1):
    s += (-1)**(i+1) * ( ( (2*i)*b )/ (divisor) )
    divisor += 3


print(f"Resultado: {round(s,6)}")