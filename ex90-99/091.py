from random import randint
players = {}
names = []
rank = []
m = []
for c in range(4):
    players['name'] = f'Jogador{c+1}'
    players['number'] = f'{randint(1,6)}'
    names.append(players.copy())
#print(names)
print('Valores sorteados:')
for c in names:
    print(f'{c['name']} tirou {c['number']} no dado.')
print('=_='*30,
    f'\n== RANKING DOS JOGADORES =='
    )
for c in names:
    rank.append(c['number'])
rank.sort()
print(rank)

for c in range(4):
    for d in names:
        if d['number'] == rank[c]:
            print(f'{c+1}º lugar: {d['name']} com {d['number']}.')