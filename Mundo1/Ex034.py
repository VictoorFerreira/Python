#PT - Escreva um programa que pergunte o sálario de um funcionário e calcule o seu aumento. (Para sálarios superiores a R$1250,00 calcule um aumento de 10% e para sálarios inferiores ou iguais, o aumento é de 15%.)
#EN - Write a program that asks an employee for his salary and calculates his salary increase. (For salaries upper than R$1250.00, calculate a 10% increase and for salaries lower than or equal to R$1250.00, the increase is 15%.)

salarie = float(input('Enter the employee salary R$: '))

upperSal = salarie + (salarie * 10 / 100) #Aumento de 10% (PT) / 10% increase (EN)
lowerSal = salarie + (salarie * 15 / 100) #Aumento de 15% (PT) / 15% increase (EN)

if salarie <= 1250:
    print('The previous salary was R${:.2f}, with the increase the salary became R${:.2f}'.format(salarie, lowerSal)) #Aumento de 10% (PT) / 10% increase (EN)
else:
    print('The previous salary was R${:.2f}, with the increase the salary became R${:.2f}'.format(salarie, upperSal)) #Aumento de 15% (PT) / 15% increase (EN)