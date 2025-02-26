#PT - Crie um programa que leia dois números e mostre a soma entre eles.
#EN - Create a program that reads two numbers and displays the sum of them.

print('-='*20)
print("Somando dois Números")
print('-='*20)
n1 = int(input('Digite primeiro numero: '))
n2 = int(input('Digite secundo numero: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))
