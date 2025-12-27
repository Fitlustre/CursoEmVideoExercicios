#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
#No final, mostre a matriz na tela, com a formatação correta.

lista = []

for c in range(3):
    if c == 0:
        for v in range(3):
            n = int(input(f'Digite um valor para [0, {v+1}]: '))
            lista.append(n)
    if c == 1:
        for v in range(3):
            n = int(input(f'Digite um valor para o [1, {v+1}]: '))
            lista.append(n)
    if c == 2:
        for v in range(3):
            n = int(input(f'Digite um valor para o [2, {v+1}]: '))
            lista.append(n)
            
print('=_='*20, '\n')
for c in range(9):
    print('[', end=' ')
    if c < 3:
        print(lista[c], end=' ] ')
    elif c > 5:
        print(lista[c],end=' ] ')
    else:
        print(lista[c], end=' ] ')
    if c == 2 or c == 5 or c == 8:
        print('\n')