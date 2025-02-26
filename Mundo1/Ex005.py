#PT - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.
#EN - Make a program that reads an integer and displays its successor and predecessor on the screen.

print('-='*20)
print('Sucessor e Antecessor')
print('-='*20)
n1 = int(input('Digite um numero: '))
ant = n1 - 1
suc = n1 + 1
print('O antecessor de {} é {}'.format(n1, ant))
print('O sucessor de {} é {}'.format(n1, suc))
