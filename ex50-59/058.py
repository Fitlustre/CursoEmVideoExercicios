# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print(
    '\033[32m'
    'Acabei de pensar num número de entre 0 e 10. \n'
    'Será que você consegue adivinhar qual foi?'
      )
n = randint(0, 10)
p = -1
c = 0
while p != n:
    p = int(input('Qual seu palpite? '))
    if 0 < p > 10:
        print('\033[33mSério, qual é a dificuldade de escrever um número de 0 a 10, ou você não sabe ler?')
    elif -1 < p < n:
        print('Mais... Tente novamente.', end='')
    elif p > n:
        print('Menos... Tente novamente.', end='')
    elif n == p:
        ""
    else:
        print('\033[31mDigite corretamente!!')
    c += 1
print('\033[1:35m=_='*16)
if c > 1:
    print(f'\033[0:34mParabens você acertou depois de {c} tentativas!!!')
elif c == 1:
    print('\033[35mCARACA DE PRIMEIRA???')
print('\033[1:35m=_='*16)
