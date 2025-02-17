import math

angulo = float(input('Digite um angulo qualquer: '))

rad = math.radians(angulo)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print('O angulo é {:.2f}º calculando o seno é {:.2f}º, cosseno é {:.2f}º e o tangente é {:.2f}º'.format(angulo, seno, cosseno,tangente))