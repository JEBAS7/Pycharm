p = float(input('Digite o valor do produto R$'))
#novo = p - (p * 5 / 100)
vd = p * 0.05
pf = p - vd
print('O produto com 5% de desconto fica R${:.2f}'.format(pf))
