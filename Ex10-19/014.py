# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.
c = float(input('Digite a temperatura em Celcius: '))
cf = c*1.8 + 32
print(f' {c}ºC são {cf:.1f}ºF.')
