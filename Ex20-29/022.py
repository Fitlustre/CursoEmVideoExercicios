#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = input('Qual seu nome completo? ').strip().title()
print(f' O seu nome é {nome};\n'
      f' Em maiúsculas fica {nome.upper()};\n'
      f' Em minúsculas fica {nome.lower()}\n'
      # Aqui eu separo o nome em uma lista e depois eu junto ele com nada.
      f' E o seu nome contêm {len(''.join(nome.split()))} letras;')
#Separo o nome em uma lista e leio o primeiro elemento da lista.
nome = nome.split()
print(f' Enquanto seu primeiro nome {nome[0]} contêm {len(nome[0])} letras.')
