from lib.arquivo import *
from lib.menu import*

arq = "cev.txt"
if fileexist(arq):
    print("Arquivo encontrado com sucesso")
else:
    criarfile(arq)

while True:
    titulo("MENU PRINCIPAL")
    menu("Ver pessoas cadastradas. Cadastrar nova Pessoa.   Eliminar base de dados. Sair do sistema")
    try:
        esc = int(input("\033[32mSua opção: \033[m"))
    except ValueError, TypeError:
        erro("Escolha uma das opções corretamente")
    except KeyboardInterrupt:
        erro("\nPrograma interrompido!")
        break
    else:
        if not 0 < esc < 5:
            erro("Opção indisponível selecione uma das opções listadas")
        else:
            if esc == 3:
                writefile(arq, '', False)
            elif esc == 1:
                readfile(arq)
            elif esc == 2:
                nome, idade = cadastro()
                writefile(arq, f"{nome.capitalize().strip():<35}{idade} anos")
            elif esc == 4:
                print("Saindo...")
                break