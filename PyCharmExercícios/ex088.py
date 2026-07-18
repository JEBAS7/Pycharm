from random import randint
from time import sleep

lista_jogos = []
dados_jogo = []

print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)

quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1

# Loop principal para gerar a quantidade de jogos pedida
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        # Garante que o número não seja repetido no mesmo jogo
        if num not in dados_jogo:
            dados_jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    dados_jogo.sort()  # Coloca o jogo em ordem crescente
    lista_jogos.append(dados_jogo[:])  # Copia o jogo para a lista principal
    dados_jogo.clear()  # Limpa para o próximo jogo
    tot += 1

print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, jogo in enumerate(lista_jogos):
    print(f'Jogo {i + 1}: {jogo}')
    sleep(1)  # Dá o efeito de sorteio em tempo real

print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
