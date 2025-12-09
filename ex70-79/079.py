
lista = list()

while True:
    n = int(input('Digite um número: '))
    if n in lista:
        print('Valor duplicado, não será adicionado!')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso!')

    while True:
        esc = input('Deseja continuar?[S/N] ').strip().lower()[0]
        if esc not in 'sn':
            print('Digite sim ou não.')
        else:
            break
    if esc == 'n':
        break

print('=_='*20)
print(f'No total foram listados {len(lista)} valores ', end='')

lista.sort()

print(lista)