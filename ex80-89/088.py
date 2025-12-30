from random import randint
from time import sleep
print('='*40)
print(f'{'JOGA NA MEGA SENA':^40}')
print('='*40)

lista = []
nj = int(input('\nQuantos jogos você quer que eu sorteie? '))
for n in range(nj):
    for c in range(6):
        while True:
            num = randint(1, 60)
            if num not in lista:
                break
        lista.append(num)
    print(f'Jogo {n+1}: {lista}')
    lista.clear()
    sleep(1)

print(f'\n{'< BOA SORTE >':=^40}')