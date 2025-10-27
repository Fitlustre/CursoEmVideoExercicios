# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.
t = ('Lápis', 5.99,
     'Caderno', 20.19,
     'Estojo', 30.00,
     'Caderno de Praia', 19.99,
     'Mochila', 49.99
     )
print('-'*40)
print(f'{'LOJA FIT':^40}')
print('-'*40)
for pos in range(len(t)):
    if pos % 2 == 0:
        print(f'{t[pos]:.<30}R$ ', end='')
    else:
        print(t[pos])
print('='*40)
