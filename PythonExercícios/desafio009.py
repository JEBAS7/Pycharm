n = int(input('Digite um número para ver a tabuada: '))
print('\nTabuada de {}'.format(n))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))