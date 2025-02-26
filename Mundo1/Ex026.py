#PT - Faça um programa que leia um frase pelo teclado e mostre
    #Quantas vezes aparece a letra a;
    #Em que posição ela aparece a primeira vez;
    #Em que posição ela aparece a ultima vez.
#EN - Make a program that reads a sentence from the keyboard and shows
    #How many times the letter a appears;
    #In which position it appears the first time;
    #In which position it appears the last time.

print('-='*20)
print('Primeira e ultima ocorrência de uma String')
print('-='*20)
frase = str(input('Digite uma frase: ')).upper()

print('Quantas vezes aparece a letra a: {}'.format(frase.count('A')))
print('Em que posição ela aparece a primeira vez: {}'.format(frase.find('A')+1))
print('Em que posição ela aparece a ultima vez: {}'.format(frase.rfind('A')+1))