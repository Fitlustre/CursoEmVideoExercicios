
def ficha(nome="<desconhecido>", golos=0):
    print(f"Jogador {nome} fez {golos} gol(s) no campeonato.")


name = input("Nome do Jogador: ")
gols = input("Gols: ")
#Gols
if gols and gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
# Nome
if name:
    ficha(nome=name, golos=gols)
else:
    ficha(golos=gols)
