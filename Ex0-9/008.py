# Escreva um programa que leia um valor em metros e exiba convertido em centímetros milímetros.
m = float(input('Digite o valor em metros: '))
mm = m * 1000
cm = m * 100
dam = m / 10
km = m / 1000
dm = m*10
m = m
hm = m / 100
print(f' {m} m \n São:\n {km} km \n {hm} hm \n {dam} dam \n {m} m \n {dm} dm \n {cm} cm \n {mm} mm')