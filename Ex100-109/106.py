def title(txt="\n"):
    tam = len(txt)
    texto =("~" * (tam+1))
    texto += "\n" + (txt.center(tam+1))
    texto += "\n" + ("~" * (tam+1))
    return  texto

def cores(txt="", tipo=None):
    if tipo and txt:
        if tipo == "title" or tipo == "t":
            print(f"\033[1;32;40m{txt}\033[m")
        elif tipo == "text" or tipo == "te":
            print(f"\033[0;34;47m{txt}\033[m")
    return None

while True:

    cores(title("Sistema de ajuda PyHelp"), "t")
    print("\033[34m", help(input("Função ou Biblioteca > ")), "\033[m")