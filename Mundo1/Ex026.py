frase = str(input('Digite uma frase: ')).upper()

print('Quantas vezes aparece a letra a: {}'.format(frase.count('A')))
print('Em que posição ela aparece a primeira vez: {}'.format(frase.find('A')+1))
print('Em que posição ela aparece a ultima vez: {}'.format(frase.rfind('A')+1))