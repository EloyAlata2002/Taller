import random as r

def generarDatos(lista, n):
    for i in range(n):
        lista.append(r.randint(1,9))

    return lista

def contarRepetidos(lista, n):
    listaAux = []
    for i in lista:
        print(f"{i} se repite: {lista.count(i)}") #.count() SIRVE PARA CONTAR NUMERO REPETIDOS EN LISTA
        if i not in listaAux:
            listaAux.append(i)
    print(listaAux) 

def numeroPrimos(lista,n):
    for i in lista:
        if i == 3:
            lista.remove(3)
            lista.insert(i,4)
        if i == 5:
            lista.remove(5)
            lista.insert(i,6)
        if i == 7:
            lista.remove(7)
            lista.insert(i,8)
    print(lista)

#SOLICITANDO DATOS
n = -1
lista = []

while n < 0 or n > 40:
    n = int(input("Ingrese la cantidad de numeros para la lista: "))

print(generarDatos(lista,n))
contarRepetidos(lista,n)
numeroPrimos(lista,n)