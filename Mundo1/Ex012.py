#PT - Faça um programa (algoritmo) que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#EN - Make a program (algorithm) that reads the price of a product and shows its new price, with a 5% discount.

print('-='*20)
print('Calculando Desconto')
print('-='*20)
preco = float(input('Digite o preço do produto: '))

npreco = preco - (preco * 0.05)

print('Seu preço anterior foi de R${:.2f} e o novo preço com desconto passou a ser de R${:.2f}' .format(preco, npreco))