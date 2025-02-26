#PT - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#EN - Create a program that reads a person's name and tells you if they have "SILVA" in their name.

print('-='*20)
print('Procurando uma string dentro da outra')
print('-='*20)
nome = str(input('Digite seu nome: ')).strip()

print('Seu nome tem silva: {}'.format('Silva' in nome))