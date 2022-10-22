import random as r
#REALIZANDO FUNCIONES
def generarDatos(lista, n):
    for i in range(n):
        lista.append(r.randint(1,9))
    print("SE GENERARON DATOS DE LA LISTA")

def mostrarDatos(lista, n):
    for i in range(n):
        print(lista[i])

def digitoRepetido(lista, n):
    print("ORDENANDO LISTA ASCENDENTEMENTE")
    lista.sort()
    print(lista)
    for i in lista:
        print(f"El numero {i} se repite {lista.count(i)}")

#DEFINIENDO DATOS
n = -1
lista = []

#VALIDANDO DATOS
while n < 0 or n > 41:
    n = int(input("Ingrese un valor para N: "))

#RESOLVIENDO A
generarDatos(lista, n)
#RESOLVIENDO B
print(lista)
#mostrarDatos(lista, n)
#RESOLVIENDO C
digitoRepetido(lista, n)
#RESOLVIENDO D
for i in lista:
    #LOS NUMEROS PRIMOS DEL 1 AL 9 SON: 2, 3, 5, 7
    if i == 3:
        pos = lista.index(i)
        lista[pos] = 4
    if i == 2:
        pos = lista.index(i)
        lista[pos] = 3
    if i == 5:
        pos = lista.index(i)
        lista[pos] = 6
    if i == 7:
        pos = lista.index(i)
        lista[pos] = 8
print("NUMEROS PRIMOS CAMBIADOS")
print(lista)