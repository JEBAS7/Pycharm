from random import randint

print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)

jogador = 0  # Contagem de vitórias começa em zero

while True:
    n = int(input('Diga um valor: '))
    palpite = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    cpu = randint(0, 10)
    soma = n + cpu

    # Define se a soma é par ou ímpar
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'

    print('-' * 60)
    print(f'Você jogou {n} e o computador jogou {cpu}. Total de {soma} DEU {resultado}')
    print('-' * 60)

    # Verifica quem ganhou
    if palpite == 'P' and resultado == 'PAR':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 30)
        jogador += 1
    elif palpite == 'I' and resultado == 'IMPAR':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 30)
        jogador += 1
    else:
        print('Você PERDEU!')
        break  # Sai do loop e encerra o jogo

print('=-' * 30)
print(f'GAME OVER! Você ganhou {jogador} vezes.')
print('=-' * 30)
