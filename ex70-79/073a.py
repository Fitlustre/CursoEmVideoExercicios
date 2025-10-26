# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

first20 = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'Vasco da Gama',
           'São Paulo', 'Red Bull Bragantino', 'Corinthians', 'Grêmio', 'Ceará', 'Internacional', 'Atlético-MG',
           'Santos', 'Vitória', 'Juventude', 'Fortaleza', 'Sport' )

print('=_='*20)
print(f'Os 20 primeiros colocados são:')
for pos, c in enumerate(first20):
    print(f'{pos+1}º {c} ')

print('=_='*20)

print('Os 5 primeiros colocados são: ')
for pos, c in enumerate(first20[:5]):
    print(f'{pos+1}º {c} ')

print('=_='*20)

print('Os últimos 4 colocados são: ')
for pos, c in enumerate(first20[19:15:-1]):
    print(f'{first20.index(c)+1}º {c}')

print('=_='*20)

print('Em ordem alfabética fica:')
for c in sorted(first20):
    print(c)
print('=_='*20)

print(f'São Paulo está na {first20.index('São Paulo')+1}ª posição.')
print('=_='*20)