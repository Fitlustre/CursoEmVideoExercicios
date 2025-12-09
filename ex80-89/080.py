# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numeros = []
final = 'Adicionado ao final da lista...'
pos = 'Adicionado na posição'
for c in range(5):
    n = int(input('Digite um número inteiro: '))
    if c == 0 or max(numeros) < n:
        numeros.append(n)
        print(final)
    else:
        if min(numeros) > n:
            numeros.insert(0, n)
            print(pos, 0, 'da lista...')
            #print(f'que é {numeros.index(n)}')
        elif n in numeros:
            numeros.insert(numeros.index(n), n)
            print(pos, numeros.index(n)+1, 'da lista...')
        else:
            for p, alg in enumerate(numeros):
                if alg > n > maior:
                    numeros.insert(p, n)
                    print(pos, numeros.index(n), 'da lista...')
                    break
                maior = alg

print(
    '=_='*20,
    f'\nOs valores digitados em ordem foram: {numeros}'
      )