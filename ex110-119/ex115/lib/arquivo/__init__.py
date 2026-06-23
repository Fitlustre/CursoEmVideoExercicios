
def fileexist(name=''):
    try:
        file = open(name, "rt")
        file.close()
    except FileNotFoundError:
        return  False
    else:
        return True

def criarfile(name=""):
    import menu
    try:
        with open(name, "wt+") as file:
            file.close()
    except Exception as error:
        menu.erro(f"Houve um ERRO ao criar {name}")
        print(error)
        exit()
    else:
        print("\033[31mArquivo criado com sucesso!\033[m")

def readfile(name):
    import menu
    try:
        file = open(name, "rt")
        file.close()
    except:
        print("Erro ao er o arquivo!")
    else:
        with open(name, "rt") as file:
            menu.titulo("PESSOAS CADASTRADAS")
            print(file.read())

def writefile(name, v='', add=True):
    if add:
        with open(name, "rt", encoding="utf-8") as file:

            txt = file.read() + "\n"
            file.close()

        with open(name, "wt", encoding="utf-8") as file:

            file.write(txt + v)
    else:
        with open(name, "wt", encoding="utf-8") as file:

            file.write(v)


def cadastro():
    import menu

    while True:
        try:
            nome = str(input("Nome: "))
        except:
            menu.erro("Digite um nome!")
        else:
            break
    while True:
        try:
            idade = int(input("Idade: "))
        except ValueError, TypeError:
            menu.erro("Digite um valor numérico")
        except KeyboardInterrupt:
            menu.erro("Programa interrompido!")
            idade = 0
            break
        else:
            break
    return nome, idade

