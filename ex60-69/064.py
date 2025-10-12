#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o Flag).
a = d = b = 0
print('Digite "999" para parar.')
while a != 999:
    b += a
    a = int(input('Digite um número:'))
    d += 1

print(f'Você digitou {d-1} números e a soma entre eles foi {b}.')
