#PT - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida a primeira e o ultimo nome separadamente.
    #Primeiro nome;
    #Ultimo nome.
#EN - Write a program that reads a person's full name, then displays the first and last names separately.
    #First name;
    #Last name.

print('-='*20)
print('Primeira e ultima nome de uma pessoa')
print('-='*20)
nome = str(input('Digite um nome completo: '))

pessoa = nome.split()
primeiro = pessoa[0]
ultimo = pessoa[len(pessoa)-1]

print('O nome da pessoa é {}'.format(nome))
print('primeiro nome é {}'.format(primeiro))
print('O ultimo nome é {}'.format(ultimo))