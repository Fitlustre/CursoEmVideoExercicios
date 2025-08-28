# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
import time
print('\033[33m='*30)
input('\033[34mVocê quer ouvir algo legal? ')
pygame.init()
pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()

print('Então ouve isto...')
# Espera enquanto a música está tocando
while pygame.mixer.music.get_busy():
    time.sleep(1)
print('\033[33m='*30)
