# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
a = float(input('\033[1:32mDigite um lado do triângulo: ')).__round__(3)
b = float(input('Digite outro lado do triângulo: ')).__round__(3)
c = float(input('Digite um último lado do triângulo: ')).__round__(3)

print('\033[35m=_=' * 30)
if a + b > c and a + c > b and b + c > a:
    print(f'\033[34mOs segmentos acima {a, b, c} PODEM FORMAR um triângulo! ', end='')
    if a == b or a == c or b == c:
        print('E é um triângulo Isósceles.')
    elif a == b == c:
        print('E é um triângulo Equilátero.')
    elif a != b != c != a:
        print('E é um triângulo escaleno.')
else:
    print(f' \033[31mOs segmentos acima não podem formar um triângulo.')

print('\033[35m=_=' * 30)
