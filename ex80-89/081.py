num = []
while True:
    num.append(int(input('Digite um número inteiro: ')))
    r = input('Deseja contnuar? [S/N]')
    if r in 'Nn':
        break
    else:
        print('\033[33mContinuando...\033[m')
print('=_='*20)
num.sort(reverse=True)
print(f'\033[34mForam digitados {len(num)} números. \nOs valores digitados em ordem crescente: {num} ')

if 5 in num:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')

