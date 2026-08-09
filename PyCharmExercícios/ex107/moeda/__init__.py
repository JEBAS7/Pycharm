def metade(n):
    return n / 2


def dobro(n):
    return n * 2


def aumentar(n, a):
    return n + a * n / 100


def diminuir(n, d):
    return n - d * n / 100


def moeda(preco, cifrao='R$'):
    # Formata com duas casas decimais e substitui o ponto da moeda americana por vírgula
    return f'{cifrao}{preco:.2f}'.replace('.', ',')
