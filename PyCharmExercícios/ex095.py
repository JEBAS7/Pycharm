jogador = dict()
gols_por_partida = list()
galera = list()  # AJUSTE 1: Lista global para salvar todos os jogadores

while True:
    jogador['nome'] = str(input('Nome: ')).strip()
    while True:
        try:
            partidas = int(input(f'Quantas partidas {jogador["nome"]}: '))
            break
        except ValueError:
            print('Por favor, digite um número inteiro válido! ')

    # 2. Laço para ler os gols de CADA partida e adicionar na lista
    for c in range(0, partidas):
        gols_da_rodada = int(input(f'   Quantos gols na {c + 1}ª partida? '))
        gols_por_partida.append(gols_da_rodada)

    # 3. Guarda a lista de gols e o total dentro do dicionário
    jogador['gols'] = gols_por_partida[:]  # Cria uma cópia da lista dentro do dicionário
    jogador['total'] = sum(gols_por_partida)  # sum() soma todos os números da lista

    galera.append(jogador.copy())  # AJUSTE 2: Salva o jogador atual na lista da galera
    gols_por_partida.clear()  # AJUSTE 3: Limpa a lista de gols para o próximo jogador

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

# --- PARTE DO PRINT DA TABELA GERAL ---
print('-' * 60)
print(f'{"cod":<4}{"nome":<10}{"gols":<15}{"total":<5}')
print('-' * 60)

# Mostra todos os jogadores cadastrados em formato de tabela
for i, j in enumerate(galera):
    print(f'{i + 1:<4}{j["nome"]:<10}{str(j["gols"]):<15}{j["total"]:<5}')
print('-' * 60)

# --- PARTE DO SISTEMA DE BUSCA DETALHADA ---

while True:
    try:
        busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
        if busca == 999:
            break
    except ValueError:
        print('Por favor, digite um número inteiro válido! ')
        continue  # <--- ADICIONE ISSO: Volta para o início do laço e ignora os testes abaixo

    # AJUSTE CORREÇÃO: Como o visual mostra 1, 2, 3... validamos se o código é maior que o tamanho da lista ou menor que 1.
    if busca > len(galera) or busca < 1:
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        # AJUSTE CORREÇÃO: Subtraímos 1 da busca para acessar o índice real correto (0, 1, 2...)
        indice_real = busca - 1
        print(f' -- LEVANTAMENTO DO JOGADOR {galera[indice_real]["nome"].upper()}:')
        for i, g in enumerate(galera[indice_real]['gols']):
            print(f'    No {i + 1}º jogo fez {g} gols.')
    print('-' * 60)

print('<< VOLTE SEMPRE >>')
