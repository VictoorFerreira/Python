import random

alunoA = str(input('Digite o nome do aluno: '))
alunoB = str(input('Digite o nome do aluno: '))
alunoC = str(input('Digite o nome do aluno: '))
alunoD = str(input('Digite o nome do aluno: '))

alunoL = [alunoA, alunoB, alunoC, alunoD]

random.shuffle(alunoL)

print('A ordem de apresentação será ')
print(alunoL)