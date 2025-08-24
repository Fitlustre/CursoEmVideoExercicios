# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
nomecd = input('Digite o nome da sua cidade: ').lower().strip()
nome = nomecd.split()
print('santo' in nome[0])
# Um outro jeito
print(nomecd[:5] == 'santo')