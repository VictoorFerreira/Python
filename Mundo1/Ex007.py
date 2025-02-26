#PT - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
#EN - Develop a program that reads a student's two grades, calculates and displays their average

print('-='*20)
print('Média Aritmética')
print('-='*20)
p1 = float(input('Digite a primeira nota: '))
p2 = float(input('Digite a segunda nota: '))
m = (p1 + p2) / 2
print('A nota da prova 1 é {:.2f} e prova 2 é {:.2f} e a sua média é {:.2f}'.format(p1, p2, m))
