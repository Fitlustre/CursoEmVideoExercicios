#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
#de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('\033[1:36m=================CONVERSSOR DE SISTEMAS=================')
n = int(input('\033[1:32mDigite um número inteiro:\033[0:32m '))
print(
      'Escolha uma das bases para conversão:\n'
      '[1] Converter para Binário\n'
      '[2] Converter para Octal\n'
      '[3] Converter para Hexadecimal'
      )

escolha = int(input('Sua escolha:\033[0:34m '))

if escolha == 1:
    print(f'{n} convertido para Binário é igual a {bin(n)[2:]}')
elif escolha == 2:
    print(f'{n} convertido para Octal é igual a {oct(n)[2:]}')
elif escolha == 3:
    print(f'{n} convertido para Hexadecimal é igual a {hex(n)[2:]}')
else:
    print('\033[31mEscolha inválida!')
print('\033[1:36m=' * 56)