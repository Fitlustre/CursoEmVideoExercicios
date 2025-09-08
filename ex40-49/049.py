#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

number = int(input('Digite um número inteiro: '))
print('\033[35m=_='*10)
for n in range(0, 11):
    print(f'\033[34m {number}x{n} = {number*n}')
print('\033[35m=_='*10)