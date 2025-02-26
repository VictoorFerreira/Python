#PT - Crie um programa que leia o nome completo de uma pessoa e mostre:
    # O nome com todas as letras MAISCULAS;
    # O nome com todas as letras MINUSCULAS;
    # Quantas letras ao todo (*sem contar os espaços);
    # Quantas letras tem o primero nome.
#EN - Create a program that reads a person's full name and displays:
    # The name with all UPPERCASE letters;
    # The name with all LOWERCASE letters;
    # How many letters in total (*without counting spaces);
    # How many letters the first name has.

print('-='*20)
print('Analisador de Texto')
print('-='*20)
nome = str(input('Digite seu nome completo: ')).strip()

nM = nome.upper()                           #Nome em Maisculas = nM (PT) / #Name in Capital Letters = nM (EN)
nm = nome.lower()                           #Nome em Minisculas = nm (PT) / #Name in Lowercase = nm (EN)
QLetrasn = len(nome) - nome.count(' ')      #Quantas letras ao todo = QLetrasn (PT) / #How many letters in total = QLetrasn (EN)


print('Seu nome em maisculas é {}'.format(nM))
print('Seu nome em maisculas é {}'.format(nm))
print('Seu nome tem ao todo {} letras'.format(QLetrasn))
separa = nome.split() #Quantas letras tem no primeiro nome (PT) / #How many letters are in the first name (EN)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))