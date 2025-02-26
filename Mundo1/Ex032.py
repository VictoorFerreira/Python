#PT - Cria um programa que leia um ano qualquer e mostre se é BISSEXTO.
#EN - Create a program that reads any year and shows if it is a LEAP year.

print('-='*20)
print('LEAP year')
print('-='*20)
import calendar
year = int(input('Enter the year: '))

if (year % 4 == 0 and year %100 != 0) or (year %400 == 0):
    print('This year you typed {}, it is a LEAP year!'.format(year))
else:
    print('This year you typed {} is NOT a LEAP year!'.format(year))