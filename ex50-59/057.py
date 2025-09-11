# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

g = str(input('Digite seu sexo: [M/F] ')).lower().strip()[0]

while g not in 'mf':
    g = str(input('Dados inválidos. Por favor , informe seu sexo: ')).lower().strip()[0]

if g == 'm':
    print('Sexo Masculino registrado com sucesso.')
elif g == 'f':
    print('Sexo Feminino registrado com sucesso.')
