def metade(n=0, formate=False):
    res = n / 2
    return res if not formate else moeda(res)


def dobro(n=0, formate=False):
    res = n * 2
    return res if not formate else moeda(res)


def aumentar(n=0, a=0, formate=False):
    res = n + (a * n / 100)
    return res if not formate else moeda(res)


def diminuir(n=0, d=0, formate=False):
    res = n - (d * n / 100)
    return res if not formate else moeda(res)


def moeda(preco=0, cifrao='R$'):
    return f'{cifrao}{preco:.2f}'.replace('.', ',')

def resumo(p, a=0, d=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)

    # Chamando as funções antigas com o "True" para formatar com a vírgula
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{a}% de aumento: \t{aumentar(p, a, True)}')
    print(f'{d}% de redução: \t{diminuir(p, d, True)}')

    print('-' * 30)
