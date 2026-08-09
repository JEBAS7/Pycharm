from random import randint

valores = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:', end='')
for numero in valores:
    print(f'{numero} ', end='')
print(f'\nO maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')
