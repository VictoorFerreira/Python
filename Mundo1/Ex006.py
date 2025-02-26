#PT - Crie um programa que leia um número e mostre o seu dobro, triplo e raiz Quadrada
#EN - Create a program that reads a number and displays its double, triple and square root.

print('-='*20)
print('Dobro, Triplo e Raiz Quadrada')
print('-='*20)
x = int(input('Digite um numero: '))
d = x * 2
t = x * 3
r = x ** (1/2)
print('O dobro de {} é {}'.format(x, d))
print('O triplo de {} é {}'.format(x, t))
print('A raiz quadrada de {} é {}'.format(x, r))
