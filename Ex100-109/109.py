from ex107.mathlib import *

n = round(float(input("Digite o preço: €")), 2)
print(
    f"A metade de {moeda(n)} é {metade(n, True)}\n"
    f"O dobro de {moeda(n)} é {dobro(n, True)}\n"
    f"Aumentando 10%, temos {aumentar(n, 10, True)}"
    )