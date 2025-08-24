#
import random
import emoji

n = random.randrange(6)
print(n)
num = int(input('Estou pensando em um número de 0 a 5, consegues adivinhar qual é? '))
if num == n:
    print('Uau você realmente acertou qual era o número kkk.')
elif num != n:
    print('Desculpa mas você errou :(')
else:
    print('Digite UM NÚMERO ENTRE 0 E 5, QUAL A DIFICULDADE????')
print(emoji.emojize('===FIM:polegar_para_cima:===', language='pt'))


