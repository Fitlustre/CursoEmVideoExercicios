from time import sleep
from random import randint
from operator import itemgetter


jogadores = {}
ranking = {}

for jogador in range(4):
    jogadores[f"jogador{jogador+1}"] = randint(1,6)

print("Valores sorteados:")
for player, dado in jogadores.items():
    print(f" {player} tirou {dado} no dado.")
    sleep(1)
#print(jogadores)

print("=_="*20)
print("== RANKING DOS JOGADORES ==")

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
#print(ranking)

for pos, j in enumerate(ranking):
    print(f"{pos+1}º lugar: {j[0]} com {j[1]}")
    sleep(1)