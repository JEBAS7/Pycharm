from random import randint

# Cria uma lista vazia para guardar os 5 números
valores = []

# Sorteia 5 números de 1 a 10 e guarda na lista
for _ in range(5):
    num = randint(1, 10)
    valores.append(num)

# Exibe os resultados
print(f'Os valores sorteados foram: {valores}')
print(f'O maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')


