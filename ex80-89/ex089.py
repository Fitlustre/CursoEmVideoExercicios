
lista = []
l_temp = []
while True:
    l_temp.append(str(input('Nome: ')))
    l_temp.append(int(input('Nota 1: ')))
    l_temp.append(int(input('Nota 2: ')))

    lista.append(l_temp[:])
    l_temp.clear()
    resp = input('Deseja continuar? [S/N]: ')[0]
    if resp in 'Nn':
        break

print(lista)