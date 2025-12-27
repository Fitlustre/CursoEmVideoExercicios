#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#No final, mostre os valores pares e ímpares em ordem crescente.

par = []
impar = []
lista = []
print('\033[34m','=_='*20)
for c in range(7):
    n = int(input(f'\033[32m Digite o {c+1}º valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
lista.append(sorted(par[:]))
lista.append(sorted(impar[:]))

print('\033[34m=_='*20)
print(
    '\033[1;32m'
    f'Os valores pares digitados foram: {lista[0]}\n'
    f'Os valores ímpares digitados foram: {lista[1]}'
    f'\033[m'
      )
