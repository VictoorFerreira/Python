#PT - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
    #Exemplo: Digite um número real: 6.27
        #O numero 6.27 tem a parte inteira 6.
#EN - Create a program that reads any real number from the keyboard and displays its whole number on the screen.
    #Example: Enter a real number: 6.27
        #The number 6.27 has the whole number 6.

print('-='*20)
print('Quebrando um número')
print('-='*20)
n = float(input('Digite um numero real: '))

pInt = int(n)
print('O numero {} tem a parte inteira {}'.format(n, pInt))