""" Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

gols = []
jogador = {"gols": gols}
num = 0

jogador["nome"] = str(input("Nome do jogador: ")).capitalize().strip()
partidas_jogadas = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))

for n in range(partidas_jogadas):
    gols.append(int(input(f"Qauntos gols na {n+1}ª partida? ")))

jogador["total"] = sum(jogador["gols"])   


# ===Primeira forma===
print("=_="*20)
print(jogador)

# ===Segunda Forma===
print("=_="*20)
for k, v in jogador.items():
    print(f'O campo "{k}" tem o valor "{v}"".')
    

# ===Terceira forma===
print("=_="*20)
print(f"O jogador {jogador["nome"]} jogou {partidas_jogadas} partidas: ")
for n, g in enumerate(jogador["gols"]):
    print(f"\t => Na {n+1}ª partida, fez {g} gols.")
print(f"Foi um total de {jogador["total"]} gols,")
