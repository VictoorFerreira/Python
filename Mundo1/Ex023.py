#PT - Faça um programa que leia um número de 0 a 9999. Mostre na tela cada um dos digitos separados. Unidade, dezena, centena, milhar
#EN - Write a program that reads a number from 0 to 9999. Display each digit separately on the screen. Unit, tens, hundreds, thousands

print('-='*20)
print('Separando digitos de um número')
print('-='*20)
n = int(input('Digite um numero entre 0 a 9999: '))
num = str(n) #convertendo o n para string (PT) / #converting n to string (EN)

unidade = num[3:4]      #unidade = num[3] (PT) / #unit = num[3] (EN)
dezena = num[2:3]       #dezena = num[2] (PT) / #tens = num[2] (EN)
centena = num[1:2]      #centena = num[1] (PT) / #hundreds = num[1] (EN)
milhar = num[:1]        #centena = num[1] (PT) / #thousands = num[1] (EN)

print('O numero digitado foi: {}'.format(n))
print('A unidade é: {}'.format(unidade))
print('A dezena é: {}'.format(dezena))
print('A centena é: {}'.format(centena))
print('A milhar é: {}'.format(milhar))