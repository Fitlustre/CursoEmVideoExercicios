# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

c = k = 0
esc = 's'
while esc in 's':
    n = int(input('Digite um número: '))
    esc = input('Quer continuar? [S/N] ').lower().strip()[0]
    c += 1
    k += n
    if c == 1:
        mev = mav = n
    else:
        if n < mev:
            mev = n
        if n > mav:
            mav = n
m = k/c
print(f'Você digitou {c} números e a média foi {m:.2f} \n'
      f'O maior valor foi {mav} e o menor foi {mev}')