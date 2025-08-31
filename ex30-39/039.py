#
from datetime import date

dia = int(input('Digite o dia que você nasceu: '))
mes = int(input('Digite o mes em que voce nasceu: '))
ano = int(input('Digite o ano em que você nasceu: '))

hoje = date.today()

nascimento = date(ano, mes, dia)

idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

if 0 < idade < 18:
    n = 18-idade
    print(f'Você tem {idade} anos de idade, ainda te faltam {n} anos para se alistar.')
elif idade == 18:
    print('Ja ta na hora de se alistar, já tens 18 anos!!!')
elif idade > 18:
    n = idade - 18
    print(f'Você tem {idade} anos, já se passaram {n} anos para o alistamento!!!')