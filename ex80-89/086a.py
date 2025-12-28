matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input((f'Digite um valor para [{l}, {c}]: ')))
print('=_='*20)
print(f' {matriz[0]} \n {matriz[1]} \n {matriz[2]}')