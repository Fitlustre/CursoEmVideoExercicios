""""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
 No final, mostre: 
 A) Quantas pessoas foram cadastradas 
 B) A média de idade 
 C) Uma lista com as mulheres 
 D) Uma lista de pessoas com idade acima da média
 """

pessoas = []

while True:
    tempdic = {}

    tempdic["nome"] = input("Nome: ")
    
    while True: # Genero
        gen = input("Sexo: [M/F] ").upper().strip()
        if not gen in "MF":
            print("\033[31mErro!\033[33m Digite apenas \"M\" ou \"F\"\033[m.")
        else:
            tempdic["genero"] = gen
            break
    
    tempdic["idade"] = int(input("Idade: "))

    pessoas.append(tempdic.copy())
    #print("Dicionario:", tempdic) # <- Debug
    #print("Lista:", pessoas)
    
    del tempdic
    
    # Exit
    while True:
        esc = input("Deseja continuar? [S/N] ").upper().strip()
        if not esc in "SN":
            pass
        else:
            break
    if esc == "N":
        break

soma_idade = 0
w = False
nomes = ""

for p in pessoas:
    soma_idade += p["idade"]
    if p["genero"] == "F":
        w = True
        nomes += p["nome"]

media_idade = round(soma_idade/len(pessoas),1)
                    
print("=_=")
print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas.")
print(f"B) A média de idade é de {media_idade} anos.")
print(f"C) As mulheres cadastradas foram {nomes}" if w else "Não foram cadastradas mulheres.")
print(f"D) Lista das pessoas cadastradas que estão a cima da média: ")
print(f'|{"NOME":^20}|{"SEXO":^20}|{"IDADE":^20}|')
print("__"*32)
for p in pessoas:
    if p["idade"] > media_idade:
        print(f'|{p["nome"].capitalize():^20}|{p["genero"].capitalize():^20}|{p["idade"]:^20}|')
        
print(f'{"<< ENCERRADO >>":^64}')