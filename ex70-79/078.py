#
valores = list()
cont = 0
for c in range(0, 5):
    cont += 1
    n = int(input(f'Digite um número [{cont}/5]: '))
    valores.append(n)


print(
    f'=_='*15,
    f'\nVocê digitou os valores {valores}\n'
    f'O maior valor foi {max(valores)} que está na {valores.index(max(valores))+1}ª posição.\n'
    f'E o menor valor foi {min(valores)} que está na {valores.index(min(valores))+1}ª posição.'
)

