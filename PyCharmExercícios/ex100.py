from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(0, 10))
        print(lista[c], end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    # Você precisa deste laço para ler número por número
    for num in lista:
        if num % 2 == 0:
            soma += num  # Agora soma 'int' com 'int' corretamente
    print(f'Somando os valores pares de {lista} temos: {soma}')


numeros = []
sorteia(numeros)
somapar(numeros)
