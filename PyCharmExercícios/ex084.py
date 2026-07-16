pessoas = list()
dados = list()

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    p = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if p == 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

# Inicializa o maior e o menor com o peso da primeira pessoa da lista
maior = menor = pessoas[0][1]

# Laço apenas para descobrir quais são os valores de maior e menor peso
for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]

# Exibe o maior peso e varre a lista para mostrar todos os que têm esse peso (trata empates)
print(f'O maior peso foi de {maior}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()  # Quebra de linha

# Exibe o menor peso e varre a lista para mostrar todos os que têm esse peso (trata empates)
print(f'O menor peso foi de {menor}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
