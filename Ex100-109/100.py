from random import*
from time import*


def sorteia(quantos_valores_sortear):
    num = quantos_valores_sortear
    lista = list()
    print(f"Sorteando {num} valores da lista: ", end=" ", flush=True)
    for c in range(num):
        n = randint(1, 10)
        lista.append(n)
        print(n, end=" ", flush=True)
        sleep(0.5)
    print("PRONTO!")

    return lista


def somarPar(valores):
    soma = 0
    for c in valores:
        if c % 2 == 0:
            soma += c
    print(f"Somando valores pares de {valores}, temos {soma}")
    
    return soma


somarPar(sorteia(5))