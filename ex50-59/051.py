#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('\033[34m=_='*10)
print('     10 TERMOS DE UMA PA')
print('=_='*10)

t = int(input('\033[32mPrimeiro termo: '))
r = int(input('Razão: \033[36m'))
#m = r * 10
m = t + (10-1) * r
for n in range(t, m+r, r):
    print(n, end=' -> ')
print('ACABOU')

#Outro genio no comentário (@nemesis9087):
p = int(input('Digite o primeiro termo: '))
rr = int(input('Digite a razão: '))
for num in range(1, 11):
    print(p, end=' ')
    p = p + r