#
while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    if t < 0:
        break
    print('-'*20)
    for c in range(1,13):
        print(f'{t} x {c} = {t*c}')
    print('-'*20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')