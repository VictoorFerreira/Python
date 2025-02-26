#PT - Crie um programa que leia o nome da cidade e diga se ela começa ou não com o nome "SANTO".
#EN - Create a program that reads the name of the city and says whether or not it starts with the name "SANTO".

print('-='*20)
print('Verificando as primeiras letras de um texto')
print('-='*20)
cidade = str(input('Digite um nome de uma cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')