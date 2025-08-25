# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = input('Digite um ano: ').strip()
ultimos_numeros = ano[2:]
ultimos_numeros = int(ultimos_numeros)
ano = int(ano)

if ultimos_numeros == 00:
    bissexto_confirm = ano / 400

    if bissexto_confirm % 1 == 0:
        print(f'{ano} é um ano Bissexto.')

    elif bissexto_confirm % 1 != 0:
        print(f'{ano} não é um ano Bissexto.')

elif ultimos_numeros != 00:
    bissexto_confirm = ultimos_numeros / 4

    if bissexto_confirm % 1 == 0:
        print(f'{ano} é um ano Bissexto.')

    elif bissexto_confirm % 1 != 0:
        print(f'{ano} não é um ano Bissexto.')

else:

    print('Confirme se digitou direito!')