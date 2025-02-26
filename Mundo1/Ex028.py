#PT - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
#EN - Write a program that makes the computer "think" of an integer between 0 and 5 and asks the user to try to figure out which number the computer chose. The program should write on the screen whether the user won or lost.

print('-='*20)
print('Guessing Game v1.0')
print('-='*20)
from random import randint
from time import sleep

comp = randint(0, 5)
print('-=-' * 20)
print('I am thinking of a number between 0 and 5. Try to guess...')
print('-=-' * 20)
player = int(input('What number did you think: '))
print('PROCESS...')
sleep(3)
if player == comp:
    print('CONGRATULATIONS! You managed to beat me!')
else:
    print('I WON! I thought of the number {} and it was not {}.'.format(comp, player))

