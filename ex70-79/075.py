# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

# Opção 1
#t = (int(input('Digite um valor')), int(input('Digite um valor')), int(input('Digite um valor')),
# int(input('Digite um valor')))
# Opção 2
t = tuple(int(input('Digite um valor: '))for c in range(0, 4))

print('Você digitou os valores: ')
for c in t:
    print(f'{c} ', end='')

print(f'\nO número 9 apareceu {t.count(9)} vezes')

if 3 in t:
    print(f'O número 3 está na {t.index(3)+1}ª posição.')
else:
    print('O número 3 não está presente.')

print('E os números pares que saíram foram: ', end='')
for c in t:
    if c % 2 == 0:
        print(f'{c} ', end='')