valores = [[], []]

for c in range(1, 8):
    # 1. Primeiro guardamos o valor digitado nesta variável 'num'
    num = int(input(f'Digite o {c}º valor: '))

    # 2. Agora testamos se o NÚMERO digitado é par
    if num % 2 == 0:
        valores[0].append(num)  # Adiciona na sublista de pares
    else:
        valores[1].append(num)  # Adiciona na sublista de ímpares

print('-=' * 30)
# sorted() mostra os números em ordem crescente
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram: {sorted(valores[1])}')
print('-=' * 30)
