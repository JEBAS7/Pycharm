valores = []

for count in range(0, 5):
    n = int(input(f'Digite um valor para a Posicão {count}: '))

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições {count}...')
print(f'O menor valor digitado foi {min(valores)} nas posições {count}...')

