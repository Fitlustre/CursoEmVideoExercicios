# Usando a biblioteca, Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
n = float(input('Digite o comprimento do cateto oposto: '))
n2 = float(input('Digite o comprimento do cateto Adjacente: '))
hipy = hypot(n, n2)
print(f'A hipotenusa é igual ou aproximadamente a {hipy:.2f}.')
