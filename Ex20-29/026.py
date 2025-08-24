#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().lower()
frase = frase.replace('á', 'a')
frase = frase.replace('â', 'a')
frase = frase.replace('ã', 'a')
frase = frase.replace('à', 'a')
print(
    f' Na sua frase a letra "A" aparece {frase.count('a')} vezes \n'
    f' E ela aparece pela primeira vez no {frase.find('a')+1}º caráctere \n'
    f' E aparece pela ultima vez no {frase.rfind('a')+1}º caráctere.'
)