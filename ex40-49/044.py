#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
print('\033[35m==========COMPRE_SEMPRE_NA_FIT-LUSTRE0=========='.replace('_', ' '))

preco = float(input('\033[1:32mPreço das compras: R$'))
print(
    'Formas de pagamento:\n'
    '[1] à vista dinheiro/cheque;\n'
    '[2] à vista cartão:\n'
    '[3] 2x no cartão;\n'
    '[4] 3x ou mais no cartão.\n'
      )
n = int(input('Qual é a opção? \033[34m'))

if n == 1:
    precos = preco - preco * 0.10
    print(f'Sua compra de R${preco:.2f} vai custar R${precos:.2f} no final.')
elif n == 2:
    precos = preco - preco * 0.05
    print(f' Sua compra de R${preco:.2f} vai custar R${precos:.2f} no final.')
elif n == 3:
    precos = preco/2
    print(f'Parcelado em 2x sem juros, sua compra de R${preco:.2f} vai custar R${precos:.2f} no final.')
elif n == 4:
    parcela = float(input('\033[1:32mDigite quantas vezes deseja parcelar:\033[34m '))
    if 2 < parcela < 12 < preco:
        precos = preco + preco * 0.2
        mes = precos / parcela
        print(
              f'Sua compra será parcelada em {parcela}x de R${mes:.2f} com juros. \n'
              f'Sua compra de R${preco:.2f} vai custar R${precos:.2f} no final.')
    else:
        print('\033[31mDigite os valores corretamente!')
else:
    print('\033[31mDigite os valores corretamente!')

print('\033[35m==========OBRIGADO_E_VOLTE_SEMPRE=========='.replace('_', ' '))