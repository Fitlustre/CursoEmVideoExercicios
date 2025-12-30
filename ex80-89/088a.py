from time import sleep
from random import randint

lista_prc = []
lista_temp = []

print('='*40)
print(f'{'JOGA NA MEGA SENA':^40}')
print('='*40)

nj = int(input('Quantos jogos você quer que eu sorteie? '))
for n in range(nj):
    for c in range(6):
        while True:
            num = randint(1, 60)
            if num not in lista_temp:
                break
        lista_temp.append(num)
    lista_prc.append(lista_temp[:])
    lista_temp.clear()
for c in range(nj):
    print(f' Jogo {c+1}: {lista_prc[c]}')
    sleep(1)
print(f'\n{'< BOA SORTE >':=^40}')