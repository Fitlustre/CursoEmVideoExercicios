#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.

print('--'*30)
print(f'{'LOJA FIT':^55}')
print('--' * 30)
t = ('Pão', 5, 'Soja', 10, 'Arroz', 1, 'Feijão',
     100, 'Tomate', 50, 'Carne', 3)
for c in t:
    if type(c) == str:
        p = 40-len(c)
        print(f'{c}', '.'*p, end=' R$ ')
    else:
        print(f'{c:.2f}')
print('=='*30)
