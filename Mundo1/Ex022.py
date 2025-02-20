nome = str(input('Digite seu nome completo: ')).strip()

nM = nome.upper()                           #Nome em Maisculas = nM
nm = nome.lower()                           #Nome em Minisculas = nm
QLetrasn = len(nome) - nome.count(' ')      #Quantas letras ao todo = QLetrasn


print('Seu nome em maisculas é {}'.format(nM))
print('Seu nome em maisculas é {}'.format(nm))
print('Seu nome tem ao todo {} letras'.format(QLetrasn))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
#maisculas = 

#minusculas = 

#letrasAoTodo = 

#letrasPrimeiroNome = 
