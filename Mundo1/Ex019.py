import random

alunoA = str(input('Digite o nome do aluno: '))
alunoB = str(input('Digite o nome do aluno: '))
alunoC = str(input('Digite o nome do aluno: '))
alunoD = str(input('Digite o nome do aluno: '))

alunoL = [alunoA, alunoB, alunoC, alunoD]

escolhido = random.choice(alunoL)

print('O aluno(a) escolhido(a) foi o(a) {}'.format(escolhido))