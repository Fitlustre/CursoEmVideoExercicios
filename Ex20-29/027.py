#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip().title().split()
print(
    f'Analisando nome...{' '.join(nome).replace(' Da ', ' da ').replace(' Dos ', ' dos ')}.\n'
    f'Olá {nome[0]} {nome[-1]}'
)
