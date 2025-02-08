sal = float(input('Digite o salario do funcionario: '))

nsal = sal + (sal * 0.15)

print('O salario anterior do funcionario e R${:.2f}, agora com aumento de 15% novo salario do funcionario e de R${:.2f}'.format(sal, nsal))