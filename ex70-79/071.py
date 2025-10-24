# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
cedula50 = cedula20 = cedula10 = cedula1 = 0
banco = 'BANCO FIT'
print('='*30)
print('        ', banco)
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
while True:

    if valor - 50 >= 0:
        valor -= 50
        cedula50 += 1
    elif valor - 20 >= 0:
        valor -= 20
        cedula20 += 1
    elif valor - 10 >= 0:
        valor -= 10
        cedula10 +=1
    elif valor - 1 >= 0:
        valor -= 1
        cedula1 += 1
    else:
        break
print(f'Para sacar R${total}, serão: ')
if cedula50 > 0:
    print(f'Um total de {cedula50} cédulas de R$50')
if cedula20 > 0:
    print(f'Um total de {cedula20} cédulas de R$20')
if cedula10 > 0:
    print(f'Um total de {cedula10} cédulas de R$10')
if cedula1 > 0:
    print(f'Um total de {cedula1} cédulas de R$1')

print('='*45)
print(f'Volte sempre ao {banco}! Tenha um bom dia!')
print('='*45)
