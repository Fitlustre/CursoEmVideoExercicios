#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('=_=' * 10)
print('Gerador de PA')
print('=_=' * 10)
d = 0
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

while d < 10:
    if d < 10:
        print(p, end=' -> ')
        p = p+r
        d += 1

print('FIM')