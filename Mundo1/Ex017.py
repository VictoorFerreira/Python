#PT - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
#EN - Make a program that reads the length of the opposite and adjacent legs of a right triangle, calculates and displays the length of the hypotenuse.

print('-='*20)
print('Cateto e Hipotenusa')
print('-='*20)
import math

catetoOposto = float(input('Digite o Cateto Oposto do triangulo Retangulo: '))
catetoAdjacente = float(input('Digite o Cateto Adjascente do triangulo Retangulo: ')) 

hipotenusa = math.sqrt(catetoOposto ** catetoOposto) + (catetoAdjacente ** catetoAdjacente)

print('O cateto Opoto e de {} e o cateto Adjascente e de {} o comprimento da hipotenusa e de {:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa))