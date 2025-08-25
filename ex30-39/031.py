# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist_viag = float(input('Quantos km andou? ')).__round__(2)

#Outro método simplificado: »»»
# preco_viagem = dist_viag * 0.50 if dist_viag<= 200 else dist_viag * 0.45

if dist_viag <= 200:
    preco_viagem = 0.50 * dist_viag
    print(f'Você andou {dist_viag:.2f}Km então terás de pagar R${preco_viagem:.2f}.')

elif dist_viag > 200:
    preco_viagem = 0.45 * dist_viag
    print(f' Você andou {dist_viag:.2f}Km então terás de pagar R${preco_viagem:.2f}.')

else:
    print('Confirme se digitou corretamente!')