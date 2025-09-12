#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Digite um número para calcular seu Fatorial: '))
s = n
f = False
print(f'Calculando !{n}', end=' = ')
while not f:
    if n > 1:
        print(n, end=' x ')
        s = s * (n - 1)
        n -= 1
    elif n == 1:
        print(n, end=' = ')
        f = True
    else:
        print('\033[31mDigite corretamente!')
        exit()
print(s)