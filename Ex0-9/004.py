#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

valor = input('\033[33mDigite um valor: ')
print('~~'*20)
print(
      '\033[36m'
      f" O seu valor é: uma {type(valor)} \n Alphanumeric: {valor.isalnum()} \n Numeric: {valor.isnumeric()} \n"
      f" Alpha: {valor.isalpha()} \n Está em maiúsculas: {valor.isupper()} \n Está em minúsculas: {valor.islower()} \n"
      f" Está capitalizada: {valor.istitle()} \n É só espaço: {valor.isspace()}"
      )
print('\033[33m~~'*20)