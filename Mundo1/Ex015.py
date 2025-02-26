#PT - Escreva um programa que pergunte a quantidade de KM (kilometros) percorridos por um carro e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
#EN - Write a program that asks for the number of KM traveled by a car and the number of days it was rented. Calculate the price to pay, knowing that the car costs R$60 per day and R$0.15 per km driven.

print('-='*20)
print('Aluguel de Carros')
print('-='*20)
kmPerc = float(input('Digite quantos kilometros foram percorridos com carro: '))    #KM(kilometros) Percorridos = kmPerc
diasAlu = int(input('Digite os dias que o carro foi alugado: ')) #Quantidade de dias alugado = diasAlu

#Sabendo que o carro custa: R$60 por dia e R$0.15 por km rodado

total = (kmPerc * 0.15) + (diasAlu * 60)    #preço a pagar = total

print('A km percorridos foram {} e os dias alugado foi {} e o total do valor foi de R${:.2f}'.format(kmPerc, diasAlu, total))