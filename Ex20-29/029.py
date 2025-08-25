#  Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#  mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
km = input('Quantos Km estava andando? ').strip().lower().replace('km', '')
km = float(km).__round__(2)  # Transforma em float e arredonda para 2 casas decimais
kms = km - 80
m = kms * 7
if km <= 80:
    print('Continue assim garoto, siga em frente.')
elif km > 400:
    print(f'COMO VOCÊ ESTA ANDANDO A MAIS DE 400KM POR HORA?\n'
          f' Toma o dobro da multa agora. \n R${m * 2:.2f} de multa')
elif km > 80:
    print(f'"Multado", agora você terá que pagar R${m:.2f} de multa por andar a {km}km por hora.')
else:
    print('Por favor verifique se escreveu corretamente, apenas números!!!')
