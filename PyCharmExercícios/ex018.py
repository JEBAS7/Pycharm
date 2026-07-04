'''import math
ang = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(ang))
co = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo {}º tem o SENO de {:.2f}'.format(ang,seno))
print('O ângulo {}º tem o COSSENO de {:.2f}'.format(ang, co))
print('O ângulo {}º tem o TANGENTE de {:.2f}'.format(ang, tan))'''

from math import radians, sin, cos, tan
ang = float(input('Digite o valor do angulo: '))
seno = sin(radians(ang))
print('O ângulo {} tem o SENO de {:.2f}'.format(ang, seno))
co = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, co))
tan = tan(radians(ang))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang, tan))


