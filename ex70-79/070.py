#
from itertools import product

total = maisdemil = n = 0
while True:
    esc = 0
    nome = input('Nome do produto: ').capitalize()
    preco = int(input('Preço do produto: R$'))
    n += 1
    total += preco

    if preco > 1000:
        maisdemil += 1

    if n == 1:
        maisbarato = preco
        menorpreco = nome

    elif maisbarato > preco:
        maisbarato = preco
        menorpreco = nome


    while esc != 's' and esc != 'n':
        esc = input('Deseja continuar? [S/N] ').lower()[0]
    if esc == 'n':
        break

print(f'Total gasto: R${total:.2f} \nProdutos mais de R$1000.00: {maisdemil} \nProduto mais barato: {menorpreco} '
      f'Preço: {maisbarato}')