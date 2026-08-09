matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0  # Caixinha para acumular a soma dos pares

# 1. LEITURA DOS DADOS (Igualzinho ao seu, perfeito!)
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30)

# 2. MOSTRAR A MATRIZ E CALCULAR OS PARES
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

        # Se o número atual for par, soma ele na caixinha
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]

    print()  # Quebra de linha ao fim de cada linha da matriz

print('-=' * 30)

# 3. CÁLCULOS FINAIS
# Sua lógica da terceira coluna estava certa! Só movi para o lugar certo.
tercol = matriz[0][2] + matriz[1][2] + matriz[2][2]

# Usamos o max() na linha 1 (que é a segunda linha) para achar o maior
maior_seg_linha = max(matriz[1])

# 4. EXIBIÇÃO DOS RESULTADOS
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {tercol}.')
print(f'O maior valor da segunda linha é {maior_seg_linha}.')

print('-=' * 30)
