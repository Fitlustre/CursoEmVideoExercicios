# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
primeiro = float(input('Primeiro Valor: '))
segundo = float(input('Segundo Valor:  '))
terceiro = float(input('Terceiro Valor: '))

if primeiro > segundo and primeiro > terceiro:
    print(f' O maior valor é o {primeiro}.')

elif segundo > primeiro and segundo > terceiro:
    print(f' O maior valor é o {segundo}')

elif terceiro > segundo and terceiro > primeiro:
    print(f' O maior valor é o {terceiro}')

if primeiro < segundo and primeiro < terceiro:
    print(f' O menor valor é o {primeiro}')

elif segundo < primeiro and segundo < terceiro:
    print(f' O menor valor é o {segundo}')

elif terceiro < primeiro and terceiro < segundo:
    print(f' O menor valor é o {terceiro}')

if primeiro == segundo and segundo == terceiro:
    print(f'Os valores são todos iguais.')
#OBS: preguiça de colocar que o maior valor é igual kkk