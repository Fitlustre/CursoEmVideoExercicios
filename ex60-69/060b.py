from math import factorial
num = int(input('Digite um número para calcular seu Fatorial: '))
print(f'Calculando !{num} = ', end='')
for n in range(num, 0, -1):
    print(n, end='')
    print(' x ' if n >1 else ' = ', end='')
print(factorial(num))
