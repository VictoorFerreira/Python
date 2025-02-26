#PT - Cria um programa que leia três números e mostre qual é o maior e qual é o menor
#EN - Create a program that reads three numbers and shows which is the largest and which is the smallest

print('-='*20)
print('Largest and Smallest Values')
print('-='*20)
n1 = int(input('Enter a number: '))
n2 = int(input('Enter a number: '))
n3 = int(input('Enter a number: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('The lowest value is {}'.format(menor)) #menor valor (PT) / lowest value (EN)
print('The greater value is {}'.format(maior)) #maior valor (PT) / greater value (EN)