# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e sua Raiz Quadrada.
n = float(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n**0.5
print(f' O Dobro de {n} é {d} \n O triplo de {n} é {t} \n E a sua Raiz Quadrada é {rq:.2f}')