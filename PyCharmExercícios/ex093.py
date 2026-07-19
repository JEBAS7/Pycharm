jogador = {}
gols_por_partida = list()  # LISTA para guardar os gols de cada partida

# 1. Coleta os dados básicos
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

# 2. Laço para ler os gols de CADA partida e adicionar na lista
for c in range(0, partidas):
    gols_da_rodada = int(input(f'   Quantos gols na {c + 1}ª partida? '))
    gols_por_partida.append(gols_da_rodada)

# 3. Guarda a lista de gols e o total dentro do dicionário
jogador['gols'] = gols_por_partida[:]  # Cria uma cópia da lista dentro do dicionário
jogador['total'] = sum(gols_por_partida)  # sum() soma todos os números da lista

# 4. Primeira saída (Visão Geral)
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)

# 5. Segunda saída (Detalhada)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

# Usamos o enumerate na lista de gols para pegar o índice (i) e a quantidade (v)
for i, v in enumerate(jogador['gols']):
    print(f'    => Na {i + 1}ª partida, fez {v} gols.')

print(f'Foi um total de {jogador["total"]} gols.')
print('=-' * 30)
