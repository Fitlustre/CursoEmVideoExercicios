#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um segundo valor: '))

e = 0
while e != 5:
    print('\033[0:37m=' * 30)
    print(
        '\033[32m'
        '[1] somar\n'
        '[2] multiplicar\n'
        '[3] maior\n'
        '[4] novos números\n'
        '[5] sair do programa')
    print('\033[0:37m='*30)

    e = int(input('\033[1:34mDecida o que fazer com os valores escolhidos: '))
    if e == 1:
        print(f'A soma entre {n1} + {n2} é igual á {n1+n2}')
    elif e == 2:
        print(f'A multiplicação entre {n1} * {n2} é igual á {n1*n2}')
    elif e == 3:

        print('O número ', end='')
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n1 == n2:
            print(f'{n1} e {n1} são iguais.')
        else:
            print(f'{n2} é maior que {n1}')
    elif e == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite um segundo valor: '))
    elif e == 5:
        print('\033[31mFinalizando...')
        sleep(3)
    else:
        print('\033[31mTente novamente...')

print('\033[34mPrograma finalizado com sucesso.')
