#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input('Digite um lado do triângulo: ')).__round__(3)
b = float(input('Digite outro lado do triângulo: ')).__round__(3)
c = float(input('Digite um último lado do triângulo: ')).__round__(3)

print('=_='*25)
if a + b > c and a + c > b and b + c > a:
    print(f'Os segmentos acima {a, b, c} PODEM FORMAR um triângulo!')

else:
    print(f' Os segmentos acima não podem formar um triângulo.')

print('=_='*25)