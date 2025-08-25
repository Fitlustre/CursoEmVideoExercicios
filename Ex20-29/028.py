#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela
# se o usuário venceu ou perdeu.
from random import randrange
import emoji
from time import sleep as dormi
n = randrange(6)
#print(n)
print('-=-'*15)
print('  Estou pensando em um número de 0 a 5...')
print('-=-'*15)

num = int(input('Consegues adivinhar qual é? '))

# Pôe o computador esperar um determinado tempo (segundos)
dormi(3)
if num == n:
    print(f'Uau você acertou qual era o número, realmente era o {n}')
elif num > 5:
    print('Digite UM NÚMERO ENTRE 0 E 5, QUAL A DIFICULDADE????')
elif num != n:
    print(f'HAHA eu GANHEI! eu pensei no número {n} não no número {num}')

print(emoji.emojize('=========FIM:polegar_para_cima:=========', language='pt'))
