matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)

tercol = matriz[0][2] + matriz[1][2] + matriz[2][2]

if pares % 2 == 0:
    print(f'A soma dos valores pares é {pares}', end='')
print()
print(f'A soma dos valores da terceira coluna é {tercol}')
print(f'O maior valor da segunda linha é {seglinha}')
