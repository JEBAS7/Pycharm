matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preenchimento da matriz (Igual ao seu)
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)

# Exibição inteligente (Substitui os seus 3 prints manuais)
for l in range(0, 3):
    for c in range(0, 3):
        # O :^5 serve para centralizar o número e deixar a matriz alinhada
        print(f'[{matriz[l][c]:^5}]', end='')
    print() # Dá uma quebra de linha ao final de cada linha da matriz
