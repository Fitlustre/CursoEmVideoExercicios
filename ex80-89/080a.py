
lista = []
for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > max(lista):
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while True:
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adionado na posição {lista.index(n)}, da lista')
                break
            pos += 1

print(f'Os valores digitados: {lista}')