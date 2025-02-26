#PT - Faça um programa (algoritmo) que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
#EN - Make a program (algorithm) that reads an employee's salary and shows his new salary, with a 15% increase.

print('-='*20)
print('Reajuste Salarial')
print('-='*20)
sal = float(input('Digite o salario do funcionario: '))     #Salário = sal

nsal = sal + (sal * 0.15)       #novo salário = nsal

print('O salario anterior do funcionario e R${:.2f}, agora com aumento de 15% novo salario do funcionario e de R${:.2f}'.format(sal, nsal))