
lista1 = []
lista2 = []
for c in range(5):
    n = int(input('Digite um valor: '))
    lista1.append(n)

for t, c in enumerate(lista1):
    if t == 0:
        lista2.append(c)
    if c >= max(lista2):
        lista2.append(c)
    elif c <= min(lista2):
        lista2.insert(1, c)
    else:
        print(f'Error{c}')

print(lista2)