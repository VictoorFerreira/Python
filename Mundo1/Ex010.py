#PT - Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
    #Considerando:US$1.00 = R$3,27
#EN - Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy.
    #Considering: US$1.00 = R$3.27

print('-='*20)
print('Conversor de Moedas')
print('-='*20)
d = int(input('Digite o valor em reais: '))
c = d / 3.27
print('Ele(a) tem na carteira R${:.2f} em reais e convertendo em doláres tem ${:.2f}'.
format(d, c))
#o valor apos a divisao esta como exemplo, para saber quanto ira ficar o valor transferencia tem que
#colocar o valor da cotação de hoje.