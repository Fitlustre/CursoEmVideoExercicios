from mathlib import *

n = round(float(input("Digite o preço: €")), 2)
print(
    f"A metade de €{n} é {metade(n):.2f}\n"
    f"O dobro de €{n} é {dobro(n):.2f}\n"
    f"Aumentando 10%, temos €{aumentar(n, 10):.2f}"
    )