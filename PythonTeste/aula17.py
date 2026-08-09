num = [2, 5, 9, 1]
num[2]  = 3
print(num)
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)
num.insert(2, 2)
print(num)
num.remove(2)
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontreio valor {v}!')
print('Cheguei ao final da lista')

# valores = list()
# for cont in range(0, 5):
    # valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontreio valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')