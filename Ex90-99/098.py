from time import*


def mostre():
    print("=_="*20)


def contador(i, f, p):
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
    sleep(2.5)
    for c in range(inicio , final , pas):
        print(c, end= ' ', flush=True)
        sleep(0.5)
    print("FIM!")

contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é a sua vez de personalizar a contagem!")
sleep(2)
contador(int(input("Início: ")), int(input("Fim: ")), int(input("Passo: ")))