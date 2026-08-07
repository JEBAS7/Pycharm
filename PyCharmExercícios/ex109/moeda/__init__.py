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
