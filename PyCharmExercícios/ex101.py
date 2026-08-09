def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    # Mantendo a regra de 65 anos proposta no Desafio 101
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa Principal (organizado como o Guanabara costuma fazer)
print()
print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
