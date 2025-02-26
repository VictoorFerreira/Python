#PT - Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
#EN - Make a program that reads any angle and displays on the screen the value of the sine, cosine and tangent of that angle.

print('-='*20)
print('Seno, Cosseno e Tangente')
print('-='*20)
import math

angulo = float(input('Digite um angulo qualquer: '))

rad = math.radians(angulo)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print('O angulo é {:.2f}º calculando o seno é {:.2f}º, cosseno é {:.2f}º e o tangente é {:.2f}º'.format(angulo, seno, cosseno,tangente))