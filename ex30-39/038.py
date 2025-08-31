#
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um outro número inteiro: '))

if n1 < n2:
    print(f'O maior valor é o {n2}')
elif n2 < n1:
    print(f'O maior valor é o {n1}')
elif n1 == n2:
    print(f'Não existe valor maior, os dois são iguais')