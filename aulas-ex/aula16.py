lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudin', 'Potato')

for c in range(0, len(lanche)): # <- Assim controla o número/posição da variável na tupla
    print(f'Eu vou comer {lanche[c]}')

for c in lanche: #  <- Assim controla diretamente o que está na variável dentro da tupla
    print(f'Eu vou comer {c}')

for pos, c in enumerate(lanche): # <- Assim podes controlar dos 2 jeitos, usando o 'pos' para a enumeração e posição
    # e usando a variável 'count' para o que está dentro da variável dentro da tupla.
    print(f'Eu vou {c} em {pos+1}º')