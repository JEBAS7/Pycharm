d = int(input('Digite a distância em Km: '))
if d <= 200:
    print('O valor da viagem é de R${:.2f}'.format(d * 0.50))
else:
    print('O valor da viagem é de R${:.2f}'.format(d * 0.45))