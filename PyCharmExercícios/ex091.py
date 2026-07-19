from random import randint
from time import sleep
from operator import itemgetter

# 1. Cria o dicionário e sorteia os valores para cada jogador
jogo = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)
}

ranking = list()

print('=== VALORES SORTEADOS ===')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)

# 2. Ordena o dicionário pelos valores (itemgetter(1)) em ordem decrescente
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('\n=== RANKING DOS JOGADORES ===')
# 3. Mostra o resultado final formatado
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
