import random
s = random.randint(0, 5)
n = int(input('digite um número entre 0 e 5: '))
if n not in range(0, 6):
    print('Erro: O número digitado está incorreto!')
if n == s:
    print('PARABENS! voçe acertou o número {}!'.format(n))
else:
    print('Voce errou, o número sorteado foi {}!.'.format(s))
