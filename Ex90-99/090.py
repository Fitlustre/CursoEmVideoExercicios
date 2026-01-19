
alunos = {}
alunos['nome'] = input('Nome: ')
alunos['media'] = round(float(input(f'Média de {alunos["nome"]}: ')), 2)
print('=_='*40)
if 0 < alunos['media'] < 5:
    print(f'{alunos[nome]} teve ma media de {alunos['media']} e está Reprovado')
elif 5 <= alunos['media'] < 7:
    print(f'{alunos[nome]} teve ma media de {alunos['media']} e está de Recuperação')
elif 7 < alunos['media'] <= 10:
    print(f'{alunos[nome]} teve ma media de {alunos['media']} e está Aprovado')
else:
    print('Erro de digitação!')