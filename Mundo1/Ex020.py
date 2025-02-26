#PT -  Crie um programa que o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos, que leia o nome dos quatros alunos e mostre a ordem sorteada.
#EN - Create a program in which the same teacher from the previous challenge wants to draw the order in which students will present their work, which reads the names of the four students and shows the order drawn.

print('-='*20)
print('Sorteando uma ordem da lista')
print('-='*20)
import random

alunoA = str(input('Digite o nome do aluno: '))
alunoB = str(input('Digite o nome do aluno: '))
alunoC = str(input('Digite o nome do aluno: '))
alunoD = str(input('Digite o nome do aluno: '))

alunoL = [alunoA, alunoB, alunoC, alunoD]       #Aluno lista = alunoL

random.shuffle(alunoL)

print('A ordem de apresentação será ')
print(alunoL)