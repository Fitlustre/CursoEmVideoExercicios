# JOKENPÔ
from random import randint
from time import sleep

itens = ('', 'PEDRA', 'PAPEL', 'TESOURA')
m = randint(1, 3)
print('\033[33m=' * 30)
print(
    '\033[32m'
    '[1] PEDRA\n'
    '[2] PAPEL\n'
    '[3] TESOURA\n'
)
j = int(input('Qual você vai escolher? '))

print('\033[35mPREPARADOS?')
sleep(1)

print('\033[33mJO', end='')
sleep(0.6)
print('KEN', end='')
sleep(0.8)
print('PÔ')
sleep(0.3)

if j < 1 or j > 3:
    print('\033[31mCOMPUTADOR VENCE POR BURRICE DO JOGADOR!')
    exit()

print('\033[35m=_=' * 10)
print(
    f'\033[34mJOGADOR ESCOLHE {itens[j]}\n'
    f'\033[36mCOMPUTADOR ESCOLHE {itens[m]}'
)
print('\033[35m=_=' * 10)

if m == j:
    print('\033[33mEMPATE')
elif m == 1:
    if j == 2:
        print('\033[34mJOGADOR VENCE!')
    elif j == 3:
        print('\033[36mCOMPUTADOR VENCE!')
elif m == 2:
    if j == 1:
        print('\033[36mCOMPUTADOR VENCE!')
    elif j == 3:
        print('\033[34mJOGADOR VENCE!')
elif m == 3:
    if j == 1:
        print('\033[34mJOGADOR VENCE!')
    elif j == 2:
        print('\033[36mCOMPUTADOR VENCE')
print('\033[33m=' * 30)