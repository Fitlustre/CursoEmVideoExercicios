# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle as ordem
nomes = input('Digite os nomes separados por espaços: ').split(' ')
ordem(nomes)
print(f' A ordem de apresentação será: {nomes}')