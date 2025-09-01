# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
n1 = int(input('\033[32mDigite um número inteiro: '))
n2 = int(input('Digite um outro número inteiro: '))


if n1 < n2:
    print(f'\033[36mO segundo valor é maior.')
elif n2 < n1:
    print(f'\033[36mO primeiro valor é maior.')
else:
    print(f'\033[36mOs dois valores são iguais.')