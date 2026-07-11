print('-' * 30)
print(f'     LOJA BISPO')
print('-' * 30)
tot_gasto = 0
tot_mil = 0
barato = 0
nome_barato = ''

while True:
    nome = str(input('Nome do Produto: ')).strip().upper()
    valor = float(input('Valor do Produto: R$'))

    # 1. Total gasto
    tot_gasto += valor

    # 2. Contagem de produtos acima de R$ 1000
    if valor > 1000:
        tot_mil += 1

    # 3. Produto mais barato
    if barato == 0 or valor < barato:
        barato = valor
        nome_barato = nome

    # Validação simples para aceitar apenas S ou N
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break

print('----- FIM DO PROGRAMA -----')
print('=-' * 20)
print(f'Total gasto na compra: R$ {tot_gasto:.2f}')
print(f'Temos {tot_mil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nome_barato} custando R${barato:.2f}')
print('=-' * 20)
