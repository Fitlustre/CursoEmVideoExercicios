
def leiaDinheiro(txt=''):
    def erro(errov=''):
        print(f"\033[31mERRO: \"{errov}\" é um preço inválido!\033[m")

    while True:
        v = input(txt).replace(',', '.')
        if v:
            teste = v.replace('.', '')
            if teste.isnumeric():
                return float(v)
            else:
                erro(v)
        else:
            erro(v)
