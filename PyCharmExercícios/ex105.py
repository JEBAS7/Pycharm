def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com várias informações sobre a situação da turma.
    """
    notas = dict()
    notas['total'] = len(n)
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['media'] = sum(n) / len(n)

    if sit:
        if notas['media'] >= 7:
            notas['situacao'] = 'BOA'  # Salva direto na chave do dicionário
        elif notas['media'] >= 5:
            notas['situacao'] = 'RAZOÁVEL'
        else:
            notas['situacao'] = 'RUIM'

    return notas


# Programa Principal
print()
print('-' * 80)
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
print()
print('-' * 80)
help(notas)

