from random import randint
pc = randint(0, 10)
c = 0
print('=_='*15)
print('        VAMOS JOGAR PAR OU ÍMPAR')
while True:
    print('=_='*15)
    esc = int(input('Digite um valor: '))
    pi = input('Par ou Ímpar? [P/I] ').lower()[0]
    r = esc + pc
    n = r % 2
    print('--' * 15)
    print(f'Você jogou {esc} e o computador {pc}. Total de {r}',
          f'DEU PAR' if n == 0 else 'DEU ÍMPAR')
    print('--' * 15)

    if pi != 'i' or pi != 'p':
        print('\033[31mDigite os valores corretamente!\033[34m')
        break
    if n == 0:
        if pi in 'p':
            print('JOGADOR VENCE')
            c += 1
        elif pi in 'i':
            print('VOCÊ PERDEU')
            break
        else:
            print('\033[31mDigite os valores corretamente!\033[37m')
    else:
        if pi in 'i':
            print('JOGADOR VENCE!')
            c += 1
        elif pi in 'p':
            print('VOCÊ PERDEU!')
            break
        else:
            print('\033[31mDigite os valores corretamente!\033[38m')
    print('Vamos jogar novamente...')
print('=_=' * 15)

print(f'GAME OVER! Você venceu {c} vezes. ')
