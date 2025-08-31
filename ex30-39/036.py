#
casa = int(input('Digite o valor da casa: '))
salario = int(input('Quanto é o seu salário? '))
anos = int(input('Em quantos anos deseja pagar a casa? '))

prestacao = casa / anos
minsal = salario * 0.3

if prestacao > minsal:
    print('Infelizmente você não tem dinheiro para financiar a casa.')
elif 0 < prestacao < minsal:
    print(f'Você tera que pagar R${prestacao:.2f} por mês.')