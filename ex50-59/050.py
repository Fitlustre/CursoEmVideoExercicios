# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
s = 0
p = 0
for c in range(1, 7):
    n = int(input(f'Digite o valor {c}: '))
    if n % 2 == 0:
        p += 1
        s += n
print(f'A soma de todos os números pares ({p}) é igual a {s}')
