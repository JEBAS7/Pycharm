from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print('A soma dos catetos {} + {} corresponde a hipotenusa {:.2f}'.format(co, ca, hi))
