n = int(input('Digite um numero entre 0 a 9999: '))
num = str(n) #convertendo o n para string

unidade = num[3:4]      #unidade = num[3]
dezena = num[2:3]       #ezena = num[2]
centena = num[1:2]      #centena = num[1]
milhar = num[:1]        #milhar = num[0] 

print('O numero digitado foi: {}'.format(n))
print('A unidade é: {}'.format(unidade))
print('A dezena é: {}'.format(dezena))
print('A centena é: {}'.format(centena))
print('A milhar é: {}'.format(milhar))