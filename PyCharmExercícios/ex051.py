primeiro = int(input('Primero termo: '))
razao = int(input('Razao: '))
décimo = primeiro + (10 - 1) * razao
for c in range(primeiro, décimo + razao, razao):
    print('{}'.format(c), end=' → ')
print('ACABOU')
