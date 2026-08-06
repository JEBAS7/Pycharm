from time import sleep

# ESTRATÉGIA VIP: Mudamos para cores de TEXTO brilhantes (91 a 96) com fundo padrão do terminal
c = [
    '\033[0m',         # 0 - sem cores (reset completo)
    '\033[1;91m',      # 1 - texto Vermelho Brilhante (para o ATÉ LOGO)
    '\033[1;92m',      # 2 - texto Verde Brilhante (para o título PyHELP)
    '\033[1;93m',      # 3 - texto Amarelo Brilhante
    '\033[1;94m',      # 4 - texto Azul Brilhante (para o 'Acessando o manual...')
    '\033[1;95m',      # 5 - texto Roxo Brilhante
    '\033[1;96m',      # 6 - texto Ciano Brilhante (para destacar o manual do help)
]


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    # Ativa o Ciano Brilhante para o manual do help ficar totalmente legível
    print(f'{c[6]}', end='')
    help(com)
    # Reseta imediatamente após o help terminar
    print(f'{c[0]}', end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    # Aplica a cor selecionada apenas no texto e nos caracteres '~'
    print(f'{c[cor]}', end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    # Reseta a cor ao fechar a moldura para não vazar para o input
    print(f'{c[0]}', end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)
