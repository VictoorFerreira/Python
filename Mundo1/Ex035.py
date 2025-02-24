#PT - Desenvolva um programa que leia o comprimento de três retas e diga ap usuário se elas podem ou não formar um triângulo.
#EN - Develop a program that reads the length of three lines and tells the user whether or not they can form a triangle.

n1 = int(input('Enter first length: '))
n2 = int(input('Enter second length: '))
n3 = int(input('Enter third length: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('The above length can FORM a triangle.')
else:
    print('The above length CANNOT FORM a triangle.')