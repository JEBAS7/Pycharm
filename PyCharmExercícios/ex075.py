valores = []
while True:
    n1 = int(input('Digite um número: '))
    valores.append(n1)
    n2 = int(input('Digite outro número: '))
    valores.append(n2)
    n3 = int(input('Digite mais um número: '))
    valores.append(n3)
    n4 = int(input('Digite o último número: '))
    valores.append(n4)

    if n4:
        break

print(f'\nVocê digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

# Cria uma lista vazia para guardar os pares
valores_pares = []

# Analisa cada número dentro da lista principal
for numero in valores:
    # O operador % (módulo) calcula o resto da divisão. Se for 0, o número é par
    if numero % 2 == 0:
        valores_pares.append(numero)

print(f'Os valores pares digitados foram {valores_pares}')
