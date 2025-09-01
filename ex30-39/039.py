# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
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