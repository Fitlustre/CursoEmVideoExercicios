
def menu(txt=""):
    """Recebe um texto separado por vírgulas e devolve as opções formatadas"""

    opcoes = txt.split(".")
    for n, op in enumerate(opcoes):
        print(f"{n+1} - {op.strip()}")

def titulo(txt=""):
    print("-"*50)
    print(txt.center(50))
    print("-" * 50)

def erro(txt=""):
    print(f"\n\033[31m{txt}\033[m")