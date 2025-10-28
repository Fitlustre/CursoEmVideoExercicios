# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
t = ('Futuro', 'Lucelio', 'Wesley', 'Castanho', 'Azulado', 'Marron', 'Python',
     'Mercado', 'CASA')
for c in t:
    print(f'\nNa palavra {c.upper()} temos:', end=' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
