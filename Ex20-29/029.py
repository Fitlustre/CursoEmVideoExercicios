#
km = float(input('Quantos Km estava andando? '))
kms = km - 80
m = kms * 7
if km <= 80:
    print('Continue assim garoto, siga em frente.')
elif km > 400:
    print(f'COMO VOCÊ ESTA ANDANDO A MAIS DE 400KM POR HORA?\n'
          f' Toma o dobro da multa agora, R${m*2:.2f} de multa')
elif km > 80:
    print(f'Boa, agora você terá que pagar R${m:.2f} de multa por andar a {km:.2f}km por hora.')
else:
    print('Por favor verifique se escreveu corretamente, apenas números!!!')