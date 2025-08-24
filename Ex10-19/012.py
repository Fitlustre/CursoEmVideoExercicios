#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
po = float(input('Qual preço do produto? '))
pn = po - po * 0.05
print(f' PARECE QUE ESTAS COM SORTE AGORA ESSE PRODUTO DE R${po} ESTA COM 5% '
      f'DE DESCONTO AGORA NO PREÇO DE R${pn:.2f}')