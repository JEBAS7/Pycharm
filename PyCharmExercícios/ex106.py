from time import sleep

# CORES ANSI: Corrigido o fechamento com 'm' no índice 7
c = [
    '\033[0m',  # 0 - Sem cores (Reset)
    '\033[1;91m',  # 1 - Vermelho Brilhante (ATÉ LOGO)
    '\033[1;92m',  # 2 - Verde Brilhante (Título PyHELP)
    '\033[1;93m',  # 3 - Amarelo Brilhante
    '\033[1;94m',  # 4 - Azul Brilhante (Acessando o manual...)
    '\033[1;95m',  # 5 - Roxo Brilhante
    '\033[1;96m',  # 6 - Ciano Brilhante (Manual do help)
    '\033[1;92;40m'  # 7 - Texto Verde Brilhante com Fundo Preto
]


def ajuda(com):
    # Usa a cor 4 (Azul) para o aviso de acesso
    título(f"Acessando o manual do comando '{com}'", 4)

    # Aplica o Ciano Brilhante (6) para o conteúdo do help() ficar legível
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    # Usa a cor passada por parâmetro (cor) em vez de fixar o 7
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')  # Reseta para o input não vir colorido
    sleep(1)


# Programa Principal
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)  # Usa o Verde Brilhante (2) para o menu
    comando = str(input('Função ou Biblioteca > ')).strip()

    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

título('ATÉ LOGO', 1)  # Usa o Vermelho Brilhante (1) para a saída
