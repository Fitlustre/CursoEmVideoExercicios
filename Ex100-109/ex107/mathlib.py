
def metade(n=0.0,formatar=False):
    if n != 0:
        n = n / 2
        return moeda(n) if formatar else n
    else:
        return None


def dobro(n=None,formatar=False):
    if n:
        n = n * 2
        return moeda(n) if formatar else n
    else:
        return None


def diminuir(n=None, p=None, formatar=False):
    if not n or not p:
        return None
    else:
        n = n - (p/100)*n
        return moeda(n) if formatar else n


def aumentar(n=None, p=None, formatar=False):
    if not n or not p:
        return None
    else:
        n = n + (p/100)*n
        return moeda(n) if formatar else n


def moeda(p=0, moedatype="€"):
    return f"{moedatype}{p:>.2f}".replace('.', ',')

