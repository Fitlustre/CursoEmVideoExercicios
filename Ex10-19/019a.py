#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
alunos = input('Digite o nome dos alunos separados por vírgulas: ').split(' ')
print(f' O escolhido foi {choice(alunos)}')
