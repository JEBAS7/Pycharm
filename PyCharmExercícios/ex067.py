while True:
    print('-' * 40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if n < 0:
        break
    print(f'\nTabuada de {n}')
    print('*=' * 8)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
    print('*=' * 8)

print('PROGRAMA TABUADA ENCERRADO. volte sempre!')
