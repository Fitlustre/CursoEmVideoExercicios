# # Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# # Exemplos de palíndromos:
# # APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

f = input('Digite uma frase: ').strip().upper().replace(' ', '')
i = f[::-1]
print(f'O inverso de {f} é {i}')
if f == i:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')