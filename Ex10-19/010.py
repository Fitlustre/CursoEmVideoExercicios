# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
r = float(input('Quanto dinheiro deseja converter? '))
us = 5.42
s = r / us
print(f' {r} R$ são {s:.2f} $')