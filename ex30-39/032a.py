# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# Versão Gustavo Guanabara
from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

# Substitui 0 pelo ano atualmente configurado no Pc.
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f' O ano {ano} é Bissexto')
else:
    print(f' O ano {ano} não é Bissexto.')
