
jogadores = []
while True:
    gols = []
    jogador = {"gols": gols}
    num = 0

    jogador["nome"] = str(input("Nome do jogador: ")).capitalize().strip()
    partidas_jogadas = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))

    for n in range(partidas_jogadas):
        gols.append(int(input(f"Qauntos gols na {n+1}ª partida? ")))

    jogador["total"] = sum(jogador["gols"])   
    
    jogadores.append(jogador.copy())
    
    while True:

        esc = input("Deseja continuar? [S/N]").lower()[0]
        if esc in "sn":
         break
        else:
           print("Digite sim ou não.")
    if esc == "n":
       break


print("=_="*30)

print("CÓDIGO", "NOME".center(15), "GOLS".ljust(15), "TOTAL")
print("--"*25)
for cod, j in enumerate(jogadores):
   cod = str(cod+1)
   print(cod.center(6), f"{j["nome"]}".center(15), f"{j['gols']}".ljust(15), j["total"])


while True:

    j = int(input("Mostrar dados de qual jogador? (999 para parar) ")) -1
    if j == 998:
        print("<< VOLTE SEMPRE! >>")
        break
    elif 0 > j or j >= len(jogadores):
        print(f"\033[31mERRO!\033[m \nNão existe jogador com o código {j+1}!")
    else:
    
        j = jogadores[j].copy()

        print(f" -- LEVANTAMENTO DO JOGADOR {j["nome"]}:")
        for ng, g in enumerate(j["gols"]):
            print(f"\tNo jogo {ng+1} fez {g} gols.")

        print("=="*30)