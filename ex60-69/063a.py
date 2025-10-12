# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
#Usando o While
t1 = 0
t2 = 1
d = 2
print('\033[34m', '--' * 15,
      '\n   Sequencia de Fibonacci\n',
      '--' * 15)

c = int(input('Quantos termos você quer mostrar? '))

# início da sequência:
if c <= 1:
    print('\033[31mEscolha um número maior que 1!')
    exit()
else:
    print('0 - 1', end=' -> ')
    while d != c:
        t3 = t1+t2
        t1 = t2
        t2 = t3
        d += 1
        print(t3, end=' -> ')
print('FIM')