
def media(valores):
    return sum(valores) / len(valores)

def notas(*n, sit=False):
    """"
    Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """

    valores = dict()
    valores["total"] = len(n)
    valores["maior"] = max(n)
    valores["menor"] = min(n)
    valores["media"] = round(media(n), 2)


    for c in n:
        if not "float" in str(type(c)) and not "int" in str(type(c)):
            return None
    if sit:
        m = valores["media"]
        if m < 5:
            situacao = "RUIM"
        elif 4 < m < 8:
            situacao = "RAZOAVEL"
        elif 7 < m < 9:
            situacao = "BOM"
        elif 9 <= m <= 10:
            situacao = "MUITO BOM"
        else:
            situacao = "Não defenido"

        valores["situacao"] = situacao

    return valores
print(notas(10, 10, 10, 6.5, sit=True))