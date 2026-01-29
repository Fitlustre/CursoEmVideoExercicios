alunos = {}
alunos['Nome:'] = input('Nome: ')
alunos['Média:'] = round(float(input(f'Média de {alunos["Nome:"]}: ')), 2)
if 0 < alunos['Média:'] < 5:
    alunos['Situação:'] = '\033[31mReprovado!\033[m'
elif 5 <= alunos['Média:'] < 7:
    alunos['Situação:'] = '\033[32mRecuperação!\033[m'
elif 7 < alunos['Média:'] <= 10:
    alunos['Situação:'] = '\033[34mAprovado!\033[m'
else:
    print('Erro de digitação!')
    exit()
print('=_='*30)
for k, v in alunos.items():
    print(f'- {k}{v}')
