# SEM USAR MUITO OS MÓDULO
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
genero = int(input('[1] Homem\n'
                   '[2] Mulher\n'
                   ))
if genero == 2:
    print('Você não precisa se alistar.')
    exit()
elif genero != 1 and genero != 2:
    print('Digite corretamente os valores')

year = date.today().year
ano = int(input('Digite seu ano de nascimento: '))

idade = year - ano
print(f'Você tem {idade} anos em {year}')
if idade < 1:
    print('Digite a idade corretamente!')
elif idade == 18:
    print('TÁ NA HORA DE SE ALISTAR RECRUTA!!!')
elif idade > 18:
    temp = idade - 18
    tempo = year - temp
    print(f'Deveria ter se alistado há {temp} anos'
          f' seu tempo de alistamento foi em {tempo}!!!'
          )
elif idade < 18:
    temp = 18 - idade
    tempo = year + temp
    print(f'Faltam {temp} anos para se alistar,'
          f' seu tempo de alistamento será em {tempo}'
          )
