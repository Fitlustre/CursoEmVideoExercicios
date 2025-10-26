# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
t = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os valores sorteados são: ', end='')
for c in t:
    print(f'{c}', end=' ')
print(f'\nO maior valor foi {max(t)}\n'
      f'E o menor valor foi {min(t)}')