from random import randint
    
players = {}
ranking = []

for jogador in range(1, 5):
    players[f'Jogador {jogador}'] = randint(1, 6)

print('Valores sorteados:')
for c in players:
    print(f'{c} tirou {players[c]} no dado.')

print('=_=' * 30)
print('== RANKING DOS JOGADORES ==')

for jogador in players:
    ranking.append((jogador, players[jogador]))

for i in range(len(ranking)):
    for j in range(i + 1, len(ranking)):
        if ranking[j][1] > ranking[i][1]:
            ranking[i], ranking[j] = ranking[j], ranking[i]

for posicao, (jogador, valor) in enumerate(ranking, start=1):
    print(f'{posicao}º lugar: {jogador} com {valor}')
