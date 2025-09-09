# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for c in range(1, 6):
    p = float(input(f'Peso da {c}º pessoa: ')).__round__(1)
    if c == 1:
        maior = p
        menor = p
    if p > maior:
        maior = p
    if p < menor:
        menor = p
print(
    f'O maior peso lido foi de {maior}Kg. \n'
    f'O menor peso lido foi de {menor}Kg.'
      )