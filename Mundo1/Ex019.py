#PT -  Crie um programa que o professor quer sortear um dos seus quatros alunos para apagar o quadro e que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
#EN - Create a program in which the teacher wants to randomly select one of his four students to erase the board and help him by reading their names and writing the name of the chosen one.

print('-='*20)
print('Sorteando um item da lista')
print('-='*20)
import random

alunoA = str(input('Digite o nome do aluno: '))
alunoB = str(input('Digite o nome do aluno: '))
alunoC = str(input('Digite o nome do aluno: '))
alunoD = str(input('Digite o nome do aluno: '))

alunoL = [alunoA, alunoB, alunoC, alunoD]       #Aluno lista = alunoL

escolhido = random.choice(alunoL)       #aluno escolhido = escolhido

print('O aluno(a) escolhido(a) foi o(a) {}'.format(escolhido))