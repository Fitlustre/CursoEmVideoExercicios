#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
n1 = input('Digite o primeiro aluno: ')
n2 = input('Digite o segundo aluno: ')
n3 = input('Digite o terceiro aluno: ')
n4 = input('Digite o quarto aluno: ')
nome = choice([n1, n2, n3, n4])
print(f'O sorteado foi: {nome:}')