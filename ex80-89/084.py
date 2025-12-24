#Faça um programa que leia nome e peso de várias pessoas,
#guardando tudo em uma lista. No final, mostre:
#   A) Quantas pessoas foram cadastradas. 
#   B) Uma listagem com as pessoas mais pesadas.
#   C) Uma listagem com as pessoas mais leves.
lista_temp = []
valores = []
peso = []
while True:

    lista_temp.append(str(input('NOME: ')))
    lista_temp.append(round(float(input('PESO: Kg ')), 2))
    valores.append(lista_temp[:])
    peso.append(lista_temp[1])
    lista_temp.clear()
    #Deseja continuar?
    resp = input('Deseja continuar?[s/n] ')
    if resp in 'Nn':
        break

maior_peso = max(peso)
menor_peso = min(peso)
#print(valores) print(peso)

print('=_='*20)
print(f'Ao todo foram registradas {len(valores)} pessoas.')
print(f'As pessoas mais pesadas, com {maior_peso}Kg foram: ', end='')
for v in valores:
    if v[1] == maior_peso:
        print(v[0], end='...')

print(f'\nAs pessoa mais leves, com {menor_peso}Kg foram: ', end='')
for c in valores:
    if c[1] == menor_peso:
        print(c[0], end='...')
print('\n', '=_='*20)
