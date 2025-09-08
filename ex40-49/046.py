#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 1,
# com uma pausa de 1 segundo entre eles.
from time import sleep
import emoji
input('\033[32mPressione Enter para começar.\033[34m')
for n in range(10, 0, -1):
    print(n)
    sleep(1)
print(emoji.emojize(':party_popper: \033[35mFeliz ano novo! :party_popper:'))