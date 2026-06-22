from ex107.mathlib import *

n = round(float(input("Digite o preço: €")), 2)
print(
    f"A metade de {moeda(n)} é {moeda(metade(n))}\n"
    f"O dobro de {moeda(n)} é {moeda(dobro(n), "R$")}\n"
    f"Aumentando 10%, temos {moeda(aumentar(n, 10))}"
    )