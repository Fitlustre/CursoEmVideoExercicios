# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
print('=====Calculador de Seno Cosseno e Tangente=====\n')
angulo = float(input('  Digite o ângulo que você deseja: '))

#Transforme em radianos, porque ele só lê em valores radianos não em graus.
rad = math.radians(angulo)

#Calcule o Seno cosseno e tangente.
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print(
    f'No ângulo {angulo}: \n'
    f' O seno vale {seno:.2f} \n O cosseno vale {cosseno:.2f} \n E a tangente vale {tangente:.2f}'
)
