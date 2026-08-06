import sys


def biblioteca(txt):
    tamanho = len(txt)

    while True:
        # Ativa fundo preto e texto verde para todo o bloco
        sys.stdout.write('\033[1;32;40m')
        sys.stdout.flush()

        # Cabeçalho do PyHELP
        print(f'{"~" * tamanho}')
        print(f'{txt}')
        print(f'{"~" * tamanho}')

        # ESTRATÉGIA PARA O PYCHARM: Exibe a mensagem como print normal (mantém fundo preto)
        print("Função ou Biblioteca (ou 'fim' para sair) > ", end='')

        # O input fica vazio, limitando a barra cinza do PyCharm apenas ao cursor de digitação
        comando = str(input()).strip()

        # Verifica a condição de parada antes do help
        if comando.upper() == 'FIM':
            print(f'{"~" * tamanho}')
            break

        # Linha decorativa antes do help
        print(f'{"~" * tamanho}')

        # Executa a ajuda (que herda perfeitamente o verde e preto)
        help(comando)

        # Linha de fechamento do bloco de ajuda
        print(f'{"~" * tamanho}\n')

    # Mensagem final totalmente envelopada na estética verde/preto
    print("PROGRAMA ENCERRADO. ATÉ LOGO!")
    print(f'{"~" * tamanho}')

    # Reseta o terminal completamente apenas após fechar tudo
    print('\033[0m', end='')


# Execução do sistema
biblioteca('        SISTEMA DE AJUDA PyHELP         ')
