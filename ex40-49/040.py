#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

n1 = float(input('Digite sua nota mais alta: ')).__round__(1)
n2 = float(input('Digite sua noa mais baixa: ')).__round__(1)

m = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a media do aluno é {m:.1f}' if n1 < 10 and n2 < 10 else m == 100)
if m < 5:
    print('\033[31mREPROVADO!')
elif 5 <= m < 7:
    print('\033[33mRECUPERAÇÃO')
elif 7 <= m <= 10:
    print('\033[34mAPROVADO!')
else:
    print('Digite os valores corretamente entre 0 e 10!')