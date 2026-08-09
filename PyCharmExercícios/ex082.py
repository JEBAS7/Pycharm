lista = []
pares = []    # Criamos uma lista vazia para os pares
impares = []  # Criamos uma lista vazia para os ímpares

while True:
    lista.append(int(input('Digite um valor: ')))

    p = ' '
    while p not in 'SN':
        p = str(input('Quer continuar? [S/N] ')).strip().upper()
        if p == '':
            p = ' '
        else:
            p = p[0]

    if p == 'N':
        break

# --- DAQUI PARA BAIXO O WHILE JÁ TERMINOU ---

# Agora percorremos a lista principal para separar os números
for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)   # Se for par, adiciona na lista de pares
    else:
        impares.append(valor) # Se não for par, adiciona na lista de ímpares

print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
