n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
fatorial = 1

# Fatorial usando for
'''for c in range(n, 0, -1):
    fatorial *= c
    print(f'{c} x ' if c > 1 else f'{c} = ', end='')
print(fatorial)'''

# Fatorial usando while
# Imprime o início da frase
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='') # Mostra o número e o sinal de x
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c            # Multiplica o resultado pelo n atual
    c -= 1                   # Diminui o c
# Imprime o último número e o resultado total
print('{}'.format(fatorial))
