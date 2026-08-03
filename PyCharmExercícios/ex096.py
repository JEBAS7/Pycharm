print(' Controle de Terrenos' .center(30))
print('-' * 30)
def area(a, b):
    m = a * b
    print(f'A área de um terreno {a}x{b} é de {m:.1f}m².')
area(a = float(input('Largura (m): ')), b = float(input('Comprimento (m): ')))
