d = int(input('quantos dias alugados: '))
km = float(input('quantos km rodados: '))
c = d * 60 + km * 0.15
print('O total a pagar é de R${:.2f}'.format(c))
