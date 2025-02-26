#PT - Escreva um programa que converta uma temperatura digigitados em ºC (graus) e converta para ºF (fahrenheit).
#EN - Write a program that converts a temperature entered in ºC (degrees) and converts it to ºF (fahrenheit).

print('-='*20)
print('Converter Temperaturas')
print('-='*20)
graus = float(input('Digite a temperatura em graus: '))

fahrenheit = 32 + (graus * 1.8)

print('A temperatura em graus e de {:.2f}º convertendo para fahrenheit e de {:.2f}º'.format(graus, fahrenheit))