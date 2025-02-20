nome = str(input('Digite um nome completo: '))

pessoa = nome.split()
primeiro = pessoa[0]
ultimo = pessoa[len(pessoa)-1]

print('O nome da pessoa é {}'.format(nome))
print('primeiro nome é {}'.format(primeiro))
print('O ultimo nome é {}'.format(ultimo))