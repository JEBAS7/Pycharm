valores = []

for count in range(0, 5):
    n = int(input(f'Digite um valor para a Posição {count}: '))
    valores.append(n)

print('=-' * 30)
print(f'Você digitou os valores {valores}')

maior = max(valores)
menor = min(valores)

# Encontra as posições do maior
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')
print()

# Encontra as posições do menor
print(f'O menor valor digitado foi {menor} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')
print()
