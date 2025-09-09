# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('\033[32mDigite um número inteiro: '))
p = 0
print('\033[35m='*30)
for c in range(1, n+1):
    m = n % c
    if m == 0:
        p += 1
        print(f'\033[34m{c}', end=' ')
    else:
        print(f'\033[31m{c}', end=' ')

if p == 2:
    print(f'\n\033[32mO número {n} foi divisível {p} vezes. \n\033[34m=> Por isso ele é um número primo.')
else:
    print(f'\n\033[32mO número {n} foi divisível {p} vezes. \n\033[31m=> Por isso ele não é um número primo.')
print('\033[35m='*30)
