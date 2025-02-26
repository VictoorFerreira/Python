#PT - Cria um programa que leia a velocidade de um carro. Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.
#EN - Create a program that reads the speed of a car. If it exceeds 80 km/h, display a message saying that the car has been fined. The fine will cost R$7.00 for each km over the limit.

print('-='*20)
print('ELECTRONIC RADAR')
print('-='*20)
vel = float(input('Enter the car speed KM/h: '))

trafficFine = (vel - 80) * 7

if vel > 80:
    print('You have been fined! The speed you were driving was {}, the speed limit is 80km/h'.format(vel))
    print('You will pay a fine in the amount of {:.2f}'.format(trafficFine))
print('Drive slowly and safely!')