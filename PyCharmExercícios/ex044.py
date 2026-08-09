print('{:=^40}'.format(' LOJAS BISPO '))
preco = float(input('Digite o valor das compras? R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preco - (preco * 10 / 100)
elif opção == 2:
    total = preco - (preco * 5 / 100)
elif opção == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preco
    print('\033[1:33mOPÇÃO INVALIDA de pagamento. Tente novamente!\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, total))
