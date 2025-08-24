# Usando a biblioteca, Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua
#porção Inteira.
from math import trunc as inteiro
num = float(input('Digite um número decimal usando o ponto não vírgula: '))
print(f'A parte inteira de {num} é {inteiro(num)}.')
