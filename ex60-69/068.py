# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
c = 0
print('=_='*15)
print('        VAMOS JOGAR PAR OU ÍMPAR')
while True:
    pi = 0
    pc = randint(0, 10)

    print('=_='*15)
    esc = int(input('Digite um valor: '))

    while pi != 'p' and pi != 'i':
        pi = input('Par ou Ímpar? [P/I] ').lower()[0]

    r = esc + pc
    n = r % 2

    print('--' * 15)
    print(f'Você jogou {esc} e o computador {pc}. Total de {r}',
          f'DEU PAR' if n == 0 else 'DEU ÍMPAR')
    print('--' * 15)

    if n == 0:
        if pi in 'p':
            print('\033[34mJOGADOR VENCE\033[38m')
            c += 1
        elif pi in 'i':
            print('\033[31mVOCÊ PERDEU\033[38m')
            break

    else:
        if pi in 'i':
            print('\033[34mJOGADOR VENCE!\033[38m')
            c += 1
        elif pi in 'p':
            print('\033[31mVOCÊ PERDEU!\033[38m')
            break

    print('\033[33mVamos jogar novamente...\033[38m')

print('=_=' * 15)

print(f'GAME OVER! Você venceu {c} vezes. ')
