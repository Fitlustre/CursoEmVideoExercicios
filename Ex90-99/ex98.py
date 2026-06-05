def mostre():
    print("=_="*20)

def contador(i, f, p):
    from time import sleep
    
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    pas = p
    final = f +1
    inicio = i

    if f - i < 0:

        pas = p - p*2
        final = f -1
    elif f == i:
        print(i)

    mostre()
    print(f"Contagem de {i} até {f} de {p} em {p}")
    for c in range(inicio , final , pas):
        print(c, end= ' ')
        sleep(0.5)
    print("FIM!")

contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é a sua vez de personalizar a contagem!")
contador(int(input("Início")).strip(), int(input("Fim")).strip(), int(input("Passo")).strip())