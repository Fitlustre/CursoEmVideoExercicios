# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

first20 = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'Vasco da Gama',
           'São Paulo', 'Red Bull Bragantino', 'Corinthians', 'Grêmio', 'Ceará', 'Internacional', 'Atlético-MG',
           'Santos', 'Vitória', 'Juventude', 'Fortaleza', 'Sport' )
print('=='*30)
print(f'Lista dos times: {first20}')
print('=='*30)
print(f'Os 5 primeiros são {first20[:5]}')
print('=='*30)
print(f'Os últimos 4 são {first20[-4:]}')
print('=='*30)
print(f'Os times em ordem alfabética {sorted(first20)}')
print('=='*30)
print(f'O São Paulo está na posição {first20.index('São Paulo')+1}')