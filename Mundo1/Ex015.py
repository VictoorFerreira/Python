kmPerc = float(input('Digite quantos kilometros foram percorridos com carro: '))
diasAlu = int(input('Digite os dias que o carro foi alugado: '))

#Sabendo que o carro custa: R$60 por dia e R$0.15 por km rodado

total = (kmPerc * 0.15) + (diasAlu * 60)

print('A km percorridos foram {} e os dias alugado foi {} e o total do valor foi de R${:.2f}'.format(kmPerc, diasAlu, total))