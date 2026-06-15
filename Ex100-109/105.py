
def media(valores):
    return sum(valores) / len(valores)

def notas(*notas, sit=False):

    valores = dict()
    valores["total"] = len(valores)
    valores["maior"] = max(notas)
    valores["menor"] = min(notas)
    valores["media"] = media(notas)


    for c in notas:
        if type(c) != float:
            return None

    return valores
print(notas(5.5, 2.5, 10, 6.5))