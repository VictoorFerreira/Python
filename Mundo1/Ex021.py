#PT - Faça um programa que abre e reproduza o áudio de um arquivo mp3.
#EN - Make a program that opens and plays the audio from an mp3 file.

print('-='*20)
print('Tocando MP3')
print('-='*20)
import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')    #Colocar o arquivo mp3 na mesma pasta do código
pygame.mixer.music.play()
pygame.event.wait()