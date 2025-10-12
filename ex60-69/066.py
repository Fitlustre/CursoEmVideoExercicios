#
c = soma = 0
print('\033[31mDigite 999 para parar.\033[38m')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    c += 1
print(f'\033[34mA soma dos {c} valores é igual a {soma}!')
