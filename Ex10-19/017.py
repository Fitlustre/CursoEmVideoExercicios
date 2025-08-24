# Sem usar a biblioteca, Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo  retângulo. Calcule e mostre o comprimento da hipotenusa.
n = float(input('Digite o comprimento do cateto oposto: '))
n2 = float(input('Digite o comprimento do cateto adjacente: '))
hipy = (n**2 + n2**2)**0.5
print(f'A hipotenusa é igual ou aproximadamente a {hipy:.2f}.')
