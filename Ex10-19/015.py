#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dia = float(input('Quantos dias você andou? '))
kms = float(input('Quantos Km você andou? '))
d = 60 * dia
km = 0.15 * kms
tp = d+km
print(f'Você tem de pagar R${tp:.2f}')
