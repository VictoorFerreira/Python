#PT - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
#EN - Make a program that reads the width and height of a wall in meters, calculates its area and the amount of paint needed to paint it, knowing that each liter of paint paints an area of ​​2m².
print('-='*20)
print('Pintando a parede')
print('-='*20)
lar = float(input('Digite a Largura da Parede: '))      #largura = lar
alt = float(input('Digite a Altura da Parde: '))        #altura = alt

ar = lar * alt      #área = ar

print('A largura da parede mede {:.2f}m e a altura da parede mede {:.2f}m e a área da parede mede {:.2f}m' .format(lar, alt, ar))