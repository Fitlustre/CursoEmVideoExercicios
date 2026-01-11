
lista = []
l_temp = []
while True:
    l_temp.append(str(input('Nome: ')))
    l_temp.append(float(input('Nota 1: ')))
    l_temp.append(float(input('Nota 2: ')))

    lista.append(l_temp[:])
    l_temp.clear()

    resp = input('Deseja continuar? [S/N]: ')[0]
    if resp in 'Nn':
        print('=_='*20)
        break

#print(lista)
print(
    '\n'
    f'Nº   NOME           MÉDIA\n',
    '-'*30
    )
for n, c in enumerate(lista):
    m = (c[1]+c[2])/2
    print(f'{n:<5}{c[0]:<15}{m:.1f}')

while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 para terminar): '))

    if aluno < len(lista):
        print(f'As notas de {lista[aluno][0]} são: {lista[aluno][1:]}')
    elif aluno == 999:
        print('\033[31mFinalizando...\033[m')
        break
    else:
        print('\033[31mValor não encontrado tente novamente!\033[m')