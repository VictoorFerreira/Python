#PT - Escreva um programa que leia um valor em metros e o exiba convertendo em centimentos e milimetros.
#EN - Write a program that reads a value in meters and displays it by converting it to centimeters and millimeters.

print('-='*20)
print('Conversor de Medidas')
print('-='*20)
n = int(input('Digite algum valor em metros: '))
c =  n * 100    #Centimentros = C
mL = n * 1000   #Milimetros = mL
print('O valor em metros é {} passando em centimentros é {}'.format(n, c))
print('O valor em metros é {} passando em milimetros é {}'.format(n, mL))
