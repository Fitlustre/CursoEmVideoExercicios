#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo
# de 1 até 500.
soma = 0
ss = 0
for n in range(0, 500, 3):
    if n % 2 == 1:
        ss += 1
        soma += n
print(f'A soma de todos os {ss} valores solicitados é {soma}')
# Ou como um GÊNIO nos comentários FEZ (@airtonsilva5271)(Youtube):
s = 0
for n in range(3, 500, 6):
    print(n)
    s += n
print(s)