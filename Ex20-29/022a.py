#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
# UM OUTRO JEITO DE FAZER

nome = input('Qual seu nome completo? ').strip().title()
print(f' O seu nome é {nome};\n'
      f' Em maiúsculas fica {nome.upper()};\n'
      f' Em minúsculas fica {nome.lower()}\n'
      f' E o seu nome contêm {len(nome) - nome.count(' ')}\n'
      f' E o seu primeiro nome contêm {nome.find(' ')} letras.')
