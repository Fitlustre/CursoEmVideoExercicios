# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
t = ('Futuro', 'Lucelio', 'Wesley', 'Castanho', 'Azulado', 'Marron', 'Python',
     'Mercado', 'CASA')
for c in t:
    print(f'\nNa palavra {c.upper()} temos:', end=' ')
    c = c.lower()
    if 'a' in c:
        print('a', end=' ')
    if 'e' in c:
        print('e', end=' ')
    if 'i' in c:
        print('i', end=' ')
    if 'o' in c:
        print('o', end=' ')
    if 'u' in c:
        print('u', end=' ')
