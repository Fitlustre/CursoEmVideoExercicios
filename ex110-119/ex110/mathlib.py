
def metade(n=0.0,formatar=False):
    if n != 0:
        n = n / 2
        return moeda(float(n)) if formatar else n
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


def moeda(p=0.0, moedatype="€"):
    return f"{moedatype}{p:>.2f}".replace('.', ',')


def resumo(preco=0, aumento=0, reducao=0, moedatype="€"):

    print('-'*32)
    print("RESUMO DO VALOR".center(32))
    print('-'*32)
    print(f"{"Preço analisando:":<23}{moeda(preco, moedatype):>}",
          f"\n{"Dobro do preço:":<23}{dobro(preco, True)}",
          f"\n{"Metade:":<23}{metade(preco, True)}",
          f"\n{aumento}{"% de aumento:":<21}{aumentar(preco, aumento, True)}",
          f"\n{reducao}{"% de redução:":<21}{diminuir(preco, reducao, True)}"
          )
