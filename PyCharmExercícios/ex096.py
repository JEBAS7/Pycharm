def area(a, b):
    m = a * b
    print(f'A área de um terreno {a}x{b} é de {m:.1f}m².')


# Programa Principal
print(' Controle de Terrenos' .center(30))
print('-' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
