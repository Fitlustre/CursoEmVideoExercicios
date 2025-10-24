# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
print('--'*20)
print('         CADASTRE UMA PESSOA')
print('--'*20)
mais18 = mulher = man = 0
while True:
    gender = esc = 0
    idade = int(input('Idade: '))
    while gender != 'f' and gender != 'm':
        gender = input('Sexo [F/M]: ').lower()[0]

    if idade > 18:
        mais18 += 1
    if gender in 'f' and idade < 20:
        mulher += 1
    elif gender in 'm':
        man += 1

    print('--'*20)
    while esc != 's' and esc != 'n':
        esc = input('Quer continuar? [S/N] ').lower()[0]
    print('--'*20)
    if esc == 'n':
        break

print('='*20)
print('FIM DO PROGRAMA')
print('='*20)

print(f' \033[34mAo todo existem {mais18} pessoas com mais de 18 anos. \n Foram cadastrados {man} homens.\n'
      f' E existem {mulher} mulheres com menos de 20 anos')
