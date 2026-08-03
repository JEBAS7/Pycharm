from time import sleep


def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(0.5)

    # 1. Mostra os números na tela um por um (como no desafio original)
    for v in num:
        print(v, end=' ', flush=True)
        sleep(0.3)

    tam = len(num)
    print(f'Foram informados {tam} valores ao todo.')

    # 2. Lógica para descobrir o maior valor
    maior_valor = 0

    for v in num:
        if v > maior_valor:
            maior_valor = v  # Atualiza o maior valor encontrado

    print(f'O maior valor informado foi {maior_valor}.')


# --- PROGRAMA PRINCIPAL ---
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()  # O desafio também pede para testar sem nenhum valor!
