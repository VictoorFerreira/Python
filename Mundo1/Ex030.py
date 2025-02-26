#PT - Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR.
#EN - Create a program that reads an integer and displays on the screen whether it is PAIR or ODD.

print('-='*20)
print('PAIR or ODD')
print('-='*20)
n = int(input('ENTER A NUMBER: '))

if n % 2 == 0:
    print('IT IS PAIR!') #PAR
else:
    print('IT IS ODD!')