# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
num = ( 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte' )
while True:

    numd = n = -1

    while True:
        numd = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numd <= 20:
            break
        print('Por favor tente novamente! ', end='')

    print(f'Você digitou o número {num[numd]}.')

    while n != 's' and n != 'n':
        n = input('Deseja continuar? [S/N] ').lower()[0]

    if n == 'n':
        break