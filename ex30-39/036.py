# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('\033[35m-=-'*32)
casa = float(input('\033[32mDigite o valor da casa: R$')).__round__(2)
salario = float(input('Quanto é o seu salário? R$')).__round__(2)
anos = int(input('Em quantos anos deseja pagar a casa? '))

prestacao = casa / (anos*12)

trintapor = salario * 0.3
print(f'Para pagar uma casa de R${casa:.2f} em sete anos a prestação será de R${prestacao:.2f}.')

if casa < 1 or salario < 1 or anos < 1:
    print('\033[33mDigite corretamente os valores!!')

elif prestacao >= trintapor:
    print('\033[31m=' * 22)
    print('||EMPRÉSTIMO NEGADO!||')
    print('=' * 22)
else:
    print('\033[34m=' * 23)
    print('||EMPRÉSTIMO APROVADO||')
    print('=' * 23)

print('\033[35m-=-'*32)