#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.                          
# C) O maior valor da segunda linha.
soma_pares = soma_t = 0
matriz = [[0,0,0], [0,0,0], [0,0,0]]
# Ordenando posições:
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        #Somando os valores pares:
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
# Somando terceira linha:
for l in range(3):
    soma_t += matriz[l][2]
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print(f'A soma dos valores pares é igual a {soma_pares}')
print(f'A soma dos valores da terceira coluna é igual a {soma_t}')
print(f'O maior valor da segunda linha é igual a {max(matriz[1])}')