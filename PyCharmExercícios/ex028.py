#Esta é minha resolução e está funcionando
'''import random
s = random.randint(0, 5)
n = int(input('digite um número entre 0 e 5: '))
if n not in range(0, 6):
    print('Erro: O número digitado está incorreto!')
if n == s:
    print('PARABENS! voçe acertou o número {}!'.format(n))
else:
    print('Voce errou, o número sorteado foi {}!.'.format(s))'''
#Resolução do professor
from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))


