#PT - Faça um programa que leia algo pelo teclado e mostre na tela e o seu tipo primitivo e todas as informações possiveis sobre ele.
#EN - Make a program that reads something from the keyboard and shows on the screen its primitive type and all possible information about it.

print('-='*20)
print('Retirando as informações de uma variável')
print('-='*20)
w = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(w))
print('Só tem espaços', w.isspace())
print('É um numerico', w.isnumeric())
print('É alfabetico', w.isalpha())
print('É alfanumerico', w.isalnum())
print('Esta em maisculo', w.isupper())
print('Esta em minusculo', w.islower())
print('Está capitalizado', w.istitle())
