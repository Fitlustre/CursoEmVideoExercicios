#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
print('=_=' * 10)
print('     Gerador de PA')
print('=_=' * 10)
d = 0
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
m = 10
tm = -1
while tm != 0:
    if d < 10:
        print(p, end=' -> ')
        p = p+r
        d += 1
    else:
        tm =int(input('\033[36mQuantos termos amais queres? \033[32m'))
        m += tm
        d -= tm
print(f'\033[34mProgressão finalizada com {m} termos mostrados.')