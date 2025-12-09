
valores = []
for c in range(5):
    valores.append(int(input(f'Digite um número para a posição {c}: ')))

maior = max(valores)
menor = min(valores)
print('='*30)
print(f'Você digitou os valores: {valores}')

#O maior
print(f'O maior valor digitado foi {maior} nas posições: ', end =' ')
for pos, v in enumerate(valores):
    if v == maior:
        print(pos, end= '...')
#O menor
print(f'\nO menor valore foi {menor} nas posições: ', end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(pos, end='...')
