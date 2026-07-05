a = int(input('Digite um ano: '))
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print('O ano {} é bissexto!'.format(a))
else:
    print('Esse ano {} não é bissexto!'.format(a))