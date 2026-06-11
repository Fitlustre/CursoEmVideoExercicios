
def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar o não a conta.
    :return: o valor do Fatorial de um número n.
    """
    
    f = 1
    result = ""
    for c in range(num, 0, -1):
        f *= c
        if show and c != 1:
            result += f"{c} x "
        elif show and c == 1:
            result += f"{c} = "
    
    if result:
        f = result + str(f)
    return f

print("_"*30)
print(fatorial(5))
help(fatorial)