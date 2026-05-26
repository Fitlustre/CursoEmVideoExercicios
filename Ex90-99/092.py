"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
 Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
 Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import datetime
trabalhador = {}

trabalhador["nome"] = str(input("Nome: ")).capitalize()


while True:
    text_error = "Por favor digite o seu ano de nascimento corretamente no formato YYYY"
    ano = int(input("Ano de nascimento: "))
    if not 0 < ano < datetime.now().year:
        print(text_error)

    else:
        idade = int(datetime.now().year) - ano
        if not 16 < idade < 60:
            print(text_error, "\nVocê não pode trabalhar com essa idade") 
        else:
            trabalhador["idade"] = idade
            break
    
cdt = int(input("Carteira de trabalho (Digite 0 se não tem): "))

if cdt != 0:
    trabalhador["Carteira de trabalho"] = cdt

    while True:
        hired = int(input("Ano de contratação: "))

        
        if not (0 < hired < datetime.now().year and (hired - ano) >= 16):
            print("\033[33mPor favor digite o ano de contratação corretamente\033[m")
        else:
            trabalhador["contratação"] = hired
            break
    
    trabalhador["salario"] = round(float(input("Salário: R$")))
    trabalhador["aposentadoria"] = f"{idade + (hired +35) - datetime.now().year} anos."

else:
    trabalhador["Carteira de trabalho"] = "Não tem"

# ===Print Final===
print("=_="*20)
for k, v in trabalhador.items():
    print(f"- {k.capitalize()}: {v}")