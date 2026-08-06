def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c}', end='') # Removi o espaço extra para alinhar com o 'x'
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='') # Adiciona o '=' quando chega no 1
    return f # RETORNA o resultado para o print do programa principal


print()
print('-' * 30)
# Programa Principal
print(fatorial(5, show=True))
print()
print('-' * 30)

# Se você tirar o comentário da linha abaixo, verá o seu manual na tela:
# help(fatorial)
