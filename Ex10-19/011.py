#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
l = float(input('Digite a largura em metros: '))
a = float(input(f'Digite a altura para calcular a área usando {l} como largura: '))
area = l * a
t = area / 2
print(f' A área da parede ({l} x {a}) é {area:.3f} cm^2 e a tinta necessária para se '
      f'pintar isso é {t:.4f} l^3')
