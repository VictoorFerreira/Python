#PT - Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da viagem, cobrando R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longas.
#EN - Develop a program that asks for the distance of a trip in KM. Calculate the price of the trip, charging R$0.50 per km for trips up to 200km and R$0.45 for longer trips.

dist = float(input('The distance of the trip in km: '))
print('You will start a journey of {}km'.format(dist))
if dist <= 200:
    price = dist * 0.50 #Distancia percorrida até 200km (PT) / Distance traveled up to 200km (EN)
else:
    price = dist * 0.45 #Distancia percorrida acima de 200km (PT) / #Distance traveled over 200km (EN)
print('The ticket price is {:.2f}'.format(price))