from random import randint
from time import sleep

dados = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)
}

print('Valores sorteados:')
for k, v in dados.items():
    print(f'O {k} tirou {v}')
    sleep(1)

# Ordenando o dicionário do maior para o menor valor
ranking = sorted(dados.items(), key=lambda item: item[1], reverse=True)

print('\nRanking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]} pontos.')
