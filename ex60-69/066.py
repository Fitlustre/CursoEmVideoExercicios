# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando a Flag).
c = soma = 0
print('\033[31mDigite 999 para parar.\033[38m')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        soma += n
        c += 1
print(f'\033[34mA soma dos {c} valores é igual a {soma}!')
