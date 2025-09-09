# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
year = date.today().year
menor = 0
maior = 0
p = int(input('Quantas pessoas são? '))
for c in range(1, p+1):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = year - ano
    if -1 < idade < 18:
        menor += 1
    elif 18 <= idade < 120:
        maior += 1
    else:
        print('\033[31mDigite o valor corretamente!')
        exit()
print(
    f'\033[34mAo todo tivemos {maior} pessoas maiores de idade!\n'
    f'\033[36mE também tivemos {menor} pessoas menores de idade!'
      )
