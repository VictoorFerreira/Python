preco = float(input('Digite o preço do produto: '))

npreco = preco - (preco * 0.05)

print('Seu preço anterior foi de R${:.2f} e o novo preço com desconto passou a ser de R${:.2f}' .format(preco, npreco))