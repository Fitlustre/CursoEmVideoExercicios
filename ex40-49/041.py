# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from datetime import date

year = date.today().year

ano = int(input('\033[32mDigite seu ano de nascimento: '))

idade = year - ano

print(f'O atleta tem {idade} anos.')
if ano < 1900:
    print('\033[31mDigite o ano corretamente!')
elif ano > year:
    print('\033[31mDigite o ano corretamente!')
elif idade <= 9:
    print(f'\033[34mClassificação: MIRIM')
elif idade <= 14:
    print('\033[34mClassificação: INFANTIL')
elif idade <= 19:
    print('\033[34mClassificação: Júnior')
elif idade <= 25:
    print('\033[34mClassificação: SÊNIOR')
elif idade > 25:
    print('\033[34mClassificação: MASTER')