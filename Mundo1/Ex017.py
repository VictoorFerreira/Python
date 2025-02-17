import math

catetoOposto = float(input('Digite o Cateto Oposto do triangulo Retangulo: '))

catetoAdjacente = float(input('Digite o Cateto Adjascente do triangulo Retangulo: ')) 

hipotenusa = math.sqrt(catetoOposto ** catetoOposto) + (catetoAdjacente ** catetoAdjacente)

print('O cateto Opoto e de {} e o cateto Adjascente e de {} o comprimento da hipotenusa e de {:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa))