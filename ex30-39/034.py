#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input(f'Digite o salário atual do funcionário: R$')).__round__(2)

if salario > 1250.00:

    aumento = 0.10 * salario + salario
    print(f' O sortudo irá ganhar um aumento de 10%, então ao invês de receber R${salario:.2f} ele receberá\n '
          f'R${aumento:.2f}')

elif salario <= 1250.00:

    aumento = 0.15 * salario + salario
    print(f'O funcionário recebera um aumento de 15%, então ao invês de receber R${salario:.2f} ele receberá\n '
          f'R${aumento:.2f}')
else:
    print('Por favor, verifique se digitou direito!')