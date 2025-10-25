#
num = ( 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte' )
numd = -1

while numd < 0 or 20 < numd:
    numd = int(input('Digite um número entre 0 e 20: '))
    if numd < 0 or 20 < numd:
        print('Por favor tente novamente! ', end='')

print(f'O número digitado, por extenso é {num[numd]}.')