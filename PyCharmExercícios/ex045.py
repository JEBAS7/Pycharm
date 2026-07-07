from random import randint
from time import sleep

# Layout corrigido com as cores ANSI e espaçamento ajustado
print('\033[1;37;40m-=-\033[m' * 20)
print('\033[1;31;47m{:^60}\033[m'.format(' JOKENPÔ '))
print('\033[1;37;40m-=-\033[m' * 20)

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é sua jogada? '))

# Verificação adicionada aqui
if jogador not in (0, 1, 2):
    print('\033[1;31mJOGADA INVÁLIDA! Tente novamente.\033[m')
else:
    print('\033[1;31;46mJO\033[m')
    sleep(1)
    print('\033[1;31;46mKEN\033[m')
    sleep(1)
    print('\033[1;31;46mPO!!!\033[m')
    print('-=' * 11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)

    if computador == 0:  # computador jogou PEDRA
        if jogador == 0:
            print('EMPATOU!')
        elif jogador == 1:
            print('JOGADOR VENCEU!')
        elif jogador == 2:
            print('COMPUTADOR VENCEU!')
    elif computador == 1:  # computador jogou PAPEL
        if jogador == 0:
            print('COMPUTADOR VENCEU!')
        elif jogador == 1:
            print('EMPATOU!')
        elif jogador == 2:
            print('JOGADOR VENCEU!')
    elif computador == 2:  # computador jogou TESOURA
        if jogador == 0:
            print('JOGADOR VENCEU!')
        elif jogador == 1:
            print('COMPUTADOR VENCEU!')
        elif jogador == 2:
            print('EMPATOU!')
