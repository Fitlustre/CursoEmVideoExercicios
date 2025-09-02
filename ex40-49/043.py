# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

peso = float(input('\033[1:32mDigite seu peso: (KG) '))
altura = float(input('Digite sua altura: (M) '))

imc = (peso / altura**2).__round__(1)
print(f'Seu IMC é de {imc}, você está em:')
if imc <= 18.5:
    print('\033[31mAbaixo do peso!!!')
elif imc <= 25:
    print('\033[32mPeso Ideal.')
elif imc <= 30:
    print('\033[34mSobrepeso!')
elif imc <= 40:
    print('\033[33mObesidade!!')
else:
    print('\033[31mObesidade Mórbida!!!')