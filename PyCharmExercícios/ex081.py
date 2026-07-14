valores = []
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)

    p = ' '
    while p not in 'SN':
        p = str(input('Quer continuar? [S/N] ')).strip().upper()
        if p == '':  # Proteção caso o usuário aperte ENTER sem digitar nada
            p = ' '
        else:
            p = p[0]

    if p == 'N':
        break

print('-=' * 30)
# 1. Mostra a quantidade de elementos
print(f'Você digitou {len(valores)} elementos.')

# 2. Mostra a ordem decrescente usando sorted()
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')

# 3. Verifica se o 5 está na lista de forma simples e direta com "in"
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
