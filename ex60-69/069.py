
pmaior = h = women = 0
while True:
    id = int(input('Digite sua idade: '))
    sex = input('Digite seu sexo[M/F]: ').lower()[0]
    if sex != 'm' and sex != 'f':
        print('\033[31mDigite os dados correctamente!\033[38m')
    else: 
        if id > 18:
            pmaior += 1
        if sex == "m":
            h += 1
        if id < 20 and sex == "f":
            women += 1
    esc = input('Quer continuar?[S/N] ').lower()[0]

    if esc == 'n':
        break
    elif esc != 's':
        print('Digite apenas S ou N.!')
print(f'Ao todo existem {pmaior} pessoas maiores de idade. \nForam cadastrados {h} homens \nE {women} mulheres com menos de 20 anos.')