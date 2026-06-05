def area(larg, comp):
    return f"{larg*comp}m²"


print("\tControle de Terrrenos\n", "--"*20)

l = round(float(input("LARGURA (m): ")), 2)
c = round(float(input("COMPRIMENTO (m): ")), 2)
print(f"A área de um terreno {l} x {c} é de {area(l, c)}")