#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randrange
from time import sleep
m = randrange(1, 3)
# MÁQUINA ESCOLHE

if m == 1:
    m = 'PEDRA'
elif m == 2:
    m = 'PAPEL'
elif m == 3:
    m = 'TESOURA'
print('[1] PEDRA\n'
      '[2] PAPEL\n'
      '[3] TESOURA\n')
j = int(input('Qual vai ser sua jogada? '))

# JOGADOR ESCOLHE
if j == 1:
    j = 'PEDRA'
elif j == 2:
    j = 'PAPEL'
elif j == 3:
    j = 'TESOURA'
elif 1 > j or j > 3:
    print('Máquina vence por burrice do jogador!')
    exit()

# JOKENPÔ
sleep(0.5)
print('\033[1mJO', end='')
sleep(0.5)
print('KEN', end='')
sleep(0.8)
print('PÔ\033[0m')
sleep(0.7)

print(f'=_='*20)
print('Máquina escolhe', m)
print('Jogador escolhe', j)
print(f'=_='*20)

if j == m:
    print('EMPATE')

elif m == 'PAPEL':

    if j == 'PEDRA':
        print('MÁQUINA VENCE!')
    elif j == 'TESOURA':
        print('JOGADOR VENCE!')

elif m == 'PEDRA':

    if j == 'PAPEL':
        print('JOGADOR VENCE!')
    elif j == 'TESOURA':
        print('MÁQUINA VENCE!')

elif m == 'TESOURA':

    if j == 'PEDRA':
        print('JOGADOR VENCE!')
    elif j == 'PAPEL':
        print('MÁQUINA VENCE!')
