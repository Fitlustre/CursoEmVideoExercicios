lista = []
while True:
    n = int(input('Digite um número inteiro: '))
    if n not in lista:
        lista.append(n)
        print('\033[34mAdicionado com sucesso!\033[m')
    else:
        print('\033[34mNúmero duplicado não será adicionado!\033[m')
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break
    else:
        print('\033[33mContinuando...\033[m')
print('=_='*20)
print(f'Você digitou os números {sorted(lista)}')