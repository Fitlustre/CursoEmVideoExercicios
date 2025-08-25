# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número inteiro: '))
if n % 2 == 1:
    print(f'{n} é impar.')
elif n % 2 == 0:
    print(f'{n} é par.')
else:
    print('Por favor digite corretamente.')