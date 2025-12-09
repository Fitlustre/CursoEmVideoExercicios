lista = []
num_par = []
num_impar = []
while True:
    lista.append(int(input('Digite um número inteiro: ')))
    r = input('Deseja contnuar? [S/N]')
    if r in 'Nn':
        break
    else:
        print('\033[33mContinuando...\033[m')
for num in lista:
    if num == 0:
        pass
    elif num % 2 == 0:
        num_par.append(num)
    else:
        num_impar.append(num)
print('=-='*20)
print(f'A lista completa é {lista}')
if len(num_impar) > 0:
    print(f'A lista de pares é {num_par}')
else:
    print('Não há números pares')
if len(num_par) > 0:
    print(f'A lista de impares é {num_impar}')
else:
    print('Não há números impares')
