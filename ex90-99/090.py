
alunos = {}
alunos['nome'] = input('Nome: ')
alunos['Média:'] = round(float(input(f'Média de {alunos["nome"]}: ')), 2)
print('=_='*40)
if 0 < alunos['Média:'] < 5:
    alunos['Situação:'] = '\033[31mReprovado!\033[m'
elif 5 <= alunos['Média:'] < 7:
    alunos['Situação:'] = '\033[32mRecuperação!\033[m'
elif 7 < alunos['Média:'] <= 10:
    alunos['Situação:'] = '\033[34mAprovado!\033[m'
else:
    print('Erro de digitação!')
    exit()
print(f'{alunos['nome']} teve ma media de {alunos['Média:']} e está {alunos['Situação:']}')
