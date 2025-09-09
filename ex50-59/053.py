# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

f = input('Digite uma frase: ').strip().upper().replace(' ', '')
m = len(f)
p = ''
for n in range(m-1, -1, -1):
    p += f[n]
print(f'O inverso de {f} é {p}')
if f == p:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
