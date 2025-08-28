# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e sua Raiz Quadrada.

cores = {
    'clean': '\033[m',
    'blue': '\033[34m',
    'yellow': '\033[33m',
    'cian': '\033[36m',
    'red': '\033[31m'
        }
n = float(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n**0.5
print(
    '\033[1m'
    f'\033[1m O Dobro de {cores['yellow']}{n:}{cores['clean']} \033[1mé {cores['yellow']}{d}{cores['clean']}'
    f' \033[1m\n O triplo de {cores['red']}{n:.3f}{cores['clean']} \033[1mé {cores['red']}{t:.3f}{cores['clean']}'
    f' \033[1m\n E a sua Raiz Quadrada é {cores['cian']}{rq:.4f}{cores['clean']}'
      )
