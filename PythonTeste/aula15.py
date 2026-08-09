n = s = 0
while n != 999:
    n = int(input('digite um numero: '))
    s += n
print('A soma vale {}'.format(s))

# loop infinito
n = s = 0
while True:
    n = int(input('digite um numero: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')

# f strings

nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')

