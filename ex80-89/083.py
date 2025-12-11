#  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#  Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
cont = expressao = 0
exp = input('Digite sua expressão: ')

for c in exp:
    if c == '(':
        cont += 1
    elif c == ')':
        cont -= 1
    if cont == -1: #caso ele comece com ")" já está errado, mas o programa do video não indentifica isso.
        expressao = 'f'
        break

if cont != 0:
    expressao = 'f'

if expressao == 'f':
    print('\033[31mSua expressão está errada!')
else:
    print('\033[34mSua expressão está correta!')