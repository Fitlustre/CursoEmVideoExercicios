#
n1 = float(input('Digite sua nota mais alta: ')).__round__(1)
n2 = float(input('Digite sua noa mais baixa: ')).__round__(1)

m = (n1 + n2) / 2

if m < 5:
    print('\033[31mREPROVADO!')
elif 4.9 < m < 7:
    print('\033[33mRECUPERAÇÃO')
elif 6.9 < m < 10.1:
    print('\033[34mAPROVADO!')