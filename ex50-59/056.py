# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
ivelho = 0
media = 0
m = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    n = input('Digite seu nome: ').title()
    i = int(input('Digite sua idade: '))
    s = input('Qual seu sexo? (M/F): ').lower().strip()
    media += i
    if i > ivelho and s == 'm':
        nvelho = n
        ivelho = i
    if s == 'f' and i < 20:
        m +=1
print(f'A média da idade do grupo é {media/4} anos.')
print(f'O homem mais velho tem {ivelho} anos e se chama {nvelho}.')
print(f'Ao todo são {m} mulheres com menos de 20 anos.')
